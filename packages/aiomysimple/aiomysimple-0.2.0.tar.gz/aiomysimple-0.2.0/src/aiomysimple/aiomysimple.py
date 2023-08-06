"""Main module."""

import aiomysql, asyncio
from functools import partial
import typing


class Row:
    def __init__(
        self, id_key: str, _row: typing.Any, conn: aiomysql.Connection, table: str
    ):
        self.id_key = id_key
        self._row = _row
        self.conn = conn
        self.table = table

    def __getattr__(self, name: str):
        return self._row[name]

    def __getitem__(self, name: str):
        return self._row[name]

    async def update(self, **kwargs):
        async with self.conn.cursor() as cur:
            await cur.execute(
                "UPDATE {} SET {} WHERE {} = %s;".format(
                    self.table,
                    ", ".join("{} = %s".format(key) for key in kwargs),
                    self.id_key,
                ),
                *kwargs.values(),
                self._row[self.id_key],
            )
        self._row.update(kwargs)


class Operation:
    operation: str

    def __init__(self, op: str, value: typing.Any):
        self.operation = op
        self.value = value

    @classmethod
    def lt(cls, value: typing.Any) -> "Operation":
        return cls("<", value)

    @classmethod
    def gt(cls, value: typing.Any) -> "Operation":
        return cls(">", value)

    @classmethod
    def eq(cls, value: typing.Any) -> "Operation":
        return cls("=", value)

    @classmethod
    def ne(cls, value: typing.Any) -> "Operation":
        return cls("!=", value)

    @classmethod
    def le(cls, value: typing.Any) -> "Operation":
        return cls("<=", value)

    @classmethod
    def ge(cls, value: typing.Any) -> "Operation":
        return cls(">=", value)

    @classmethod
    def not_(cls, value: typing.Any) -> "Operation":
        return cls("NOT", value)

    @classmethod
    def order_by(cls, key: str) -> "Operation":
        return cls("ORDER BY", key)

    @classmethod
    def any_of(cls, *args, **kwargs) -> "Operation":
        if args and not kwargs:
            return cls("IN", args)
        elif kwargs and not args:
            return cls("AnyOf", kwargs)
        else:
            raise TypeError("invalid query for any_of")

    def __repr__(self) -> str:
        if self.operation == "IN":
            return "IN(" + ", ".join(normalise(i) for i in self.value) + ")"
        elif self.operation == "AnyOf":
            return "({})".format(
                " OR ".join(kw_to_query(k, v) for k, v in self.value.items())
            )
        else:
            return self.operation + normalise(self.value)


def normalise(value: typing.Any) -> str:
    if isinstance(value, bool):
        return repr(value).lower()
    elif value is None:
        return "null"
    else:
        return repr(value)


def kw_to_query(name: str, value: typing.Union[Operation, str]) -> str:
    if isinstance(value, str):
        value = Operation.eq(value)
    return name + repr(value)


class SearchIterator:
    def __init__(self, query: str, conn: aiomysql.Connection, table: str, id_key: str):
        self.conn = conn
        self.query = query
        self.table = table
        self.id_key = id_key

    async def __aiter__(self):
        async with self.conn.cursor(aiomysql.SSDictCursor) as cur:
            await cur.execute(self.query)
            for _ in range(cur.arraysize):
                yield Row(self.id_key, await cur.fetchone(), self.conn, self.table)

    async def __getitem__(self, index: int):
        if not isinstance(index, int):
            raise TypeError("cannot index with non-integer value {:!r}".format(index))
        async with self.conn.cursor(aiomysql.SSDictCursor) as cur:
            await cur.execute(self.query)
            await cur.scroll(index, "absolute")
            return Row(self.id_key, await cur.fetchone(), self.conn, self.table)


class Table:
    def __init__(self, connection: aiomysql.Connection, table_name: str, id_key: str):
        self.connection = connection
        self.table_name = table_name
        self.id_key = id_key

    async def get(self, *args, **kwargs):
        args = list(args)
        order_by = None
        if args and isinstance(args[0], Operation) and args[0].operation == "ORDER BY":
            order_by = args.pop(0).value
        if args or kwargs:
            query = "SELECT {} FROM {}{} WHERE {};".format(
                self.id_key,
                self.table_name,
                f" ORDER BY {order_by}" if order_by else "",
                " AND ".join(*args, *[kw_to_query(k, v) for k, v in kwargs.items()]),
            )
        else:
            query = "SELECT {} FROM {}{};".format(
                self.id_key,
                self.table_name,
                f" ORDER BY {order_by}" if order_by else "",
            )
        async with self.connection.cursor(aiomysql.DictCursor) as cursor:
            await cursor.execute(query)
            if cursor.arraysize > 1:
                raise TypeError("more than one unique row for this get()")
            elif cursor.arraysize == 1:
                return Row(
                    self.id_key,
                    await cursor.fetchone(),
                    self.connection,
                    self.table_name,
                )
            else:
                return None

    async def search(self, *args, **kwargs):
        order_by = None
        args = list(args)
        if args and isinstance(args[0], Operation) and args[0].operation == "ORDER BY":
            order_by = args.pop(0).value
        if args or kwargs:
            query = "SELECT {} FROM {}{} WHERE {};".format(
                self.id_key,
                self.table_name,
                f" ORDER BY {order_by}" if order_by else "",
                " AND ".join(
                    *args[1:], *[kw_to_query(k, v) for k, v in kwargs.items()]
                ),
            )
        else:
            query = "SELECT {} FROM {}{};".format(
                self.id_key,
                self.table_name,
                f" ORDER BY {order_by}" if order_by else "",
            )
        return SearchIterator(query, self.connection, self.table_name, self.id_key)


class Database:
    def __init__(self, host: str, port: int, user: str, password: str, database: str):
        asyncio.get_event_loop().create_task(
            self._init(
                host=host, port=port, user=user, password=password, database=database
            )
        )

    async def _init(
        self, host: str, port: int, user: str, password: str, database: str
    ):
        self.connection = await aiomysql.connect(
            host=host, port=port, user=user, password=password, autocommit=True,
        )

    def get_table(self, table_name: str, id_key):
        return Table(self.connection, table_name, id_key)

    def __del__(self):
        asyncio.get_event_loop().create_task(self.connection.close())

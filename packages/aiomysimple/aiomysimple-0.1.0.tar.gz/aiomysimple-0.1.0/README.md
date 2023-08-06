# AioMySimple

[![Licence: GPL v3](https://img.shields.io/badge/Licence-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

AioMySimple is a simpler interface for AioMySQL

```py
import aiomysimple

db = aiomysimple.Database(
    host="127.0.0.1", port=3306, user="root", password="", db="test_pymysql"
)
my_table = db.get_table("my_table", "id")
async for row in await my_table.search():
    print(row["my_key"])
    await row.update(my_key=row["my_key"] + 1)
result = await my_table.search()
print((await result[3])["my_key"])
```

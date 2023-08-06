#!/usr/bin/env python

from setuptools import setup, find_packages  # type: ignore
from src.aiomysimple import __version__

with open("README.md") as readme_file:
    readme = readme_file.read()
with open("requirements.txt") as requirements_file:
    requirements = requirements_file.read().splitlines()

setup(
    author="Starwort",
    author_email="tcphone93@gmail.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
    description="A simpler wrapper for aiomysql",
    install_requires=[],
    license="GNU General Public License v3",
    long_description=readme,
    long_description_content_type="text/markdown",
    package_data={"aiomysimple": ["py.typed"]},
    include_package_data=True,
    keywords="aiomysimple",
    name="aiomysimple",
    package_dir={"": "src"},
    packages=find_packages(include=["src/aiomysimple", "src/aiomysimple.*"]),
    setup_requires=requirements,
    url="https://github.com/Starwort/aiomysimple",
    version=__version__,
    zip_safe=False,
)

# Overview

The software that I wrote is an SQL relational database and interface using Python. In conjunction I used an imported sqlite3 library.
The database contains Star Wars ship information. Raw data was pulled from an authoritative source and inputted into the database via sqlite3.
An interface is included to allow CRUD operations to be performed on the included database. The user interface displays different options to run operations.
Each choice is prefix number, then selected via user input. Specific data types are required upon input because the database columns use an explicit data type.

The purpose for writing this software was to implement SQL relational database functionality into Python. This software serves as a demonstration
on how to use an included Python library, sqlite3. In sqlite3 we can perform CRUD operations as in MySQL workbench. The advantage to using sqlite3
is that it is much easier to connect with our database. There isn't any required setup as in Workbench prior to interacting with a database.
This software provides instruction on how to query a database, insert data into a table, creating a new database and/ or table, and deleting data.
 
[Software Demo Video](https://youtu.be/KjhwHPjnsQ4)


# Relational Database

I created the relational database that is being used in this software. It is a Star Wars ship database
consiting of raw data. It follows 3NF design format for compatible use.

There is one entity in our database, one table contains all of the data.
Sqlite3 incorporates default rowid's for each row of data acting as a primary key.


# Development Environment

  Tools:
- VSCode
- Library: sqlite3


# Useful Websites

* [YouTube](https://www.youtube.com/watch?v=byHcYRpMgI4&list=WL&index=19&t=2113s)
* [SQLite Tutorial](https://www.sqlitetutorial.net/)
* [w3resource] (https://www.w3resource.com/sqlite/)
* [SQLite] (https://www.sqlite.org/index.html)


# Future Work

* Item 1: Add - I want to add JOINs using designated foreign and primary keys
* Item 2: Fix - The formatting of the output is not completely seemless. I used a few workarounds to get a clean output to the user. But there are still a few kinks to work out
		to make the output consistent.
* Item 3: Add - I would like to add more tables that follow 3NF design principles. 
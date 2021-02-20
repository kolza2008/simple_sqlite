# simple_sqlite
Library for simplify work with sqlite3


Main target for this library is abstract from 
routine is associated with work with database,
but don't delete work with requests. 
If you want delete work with requests, we can 
use **simple_sqlite.helper**.

## Simplify your database
You can simplify work with database with module
**simple_sqlite.simplifer**. To get started work with it, 
you need init class *AdvancedDispatcher*.
```
import sqlite3 
import simple_sqlite.simplifer as disp

conn = sqlite3.connect('db.db')
cur = conn.cursor()
disp = disp.AdvancedDispatcher(conn, cur)
```

Most important things in database is writing to database and 
reading from it. To write to it and read from it, package provides
decorators *write* and *read*. In method, you must write only
request. Library execute all routine.
```
@disp.write
def new_book():
  return "INSERT INTO books (name) VALUES 'War and peace'"
  
@disp.read
def all_books():
  return 'SELECT * FROM books'
```

Often you need to init your database, that is to create table,
config it and etc. For this, class *AdvancedDispatcher* provides
decorator *init*
```
@disp.init
@disp.write
def create_books():
  return 'CREATE TABLE books(id PRIMARY KEY AUTOINCREMENT, name STRING)'
```

To start initial methods, you must run method *AdvancedDispatcher.start*
```
disp.start()
```

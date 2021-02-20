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

from dataclasses import *

@dataclass
class Table:
    name: str
    columns: str
    request: str

def new_table(table:str, columns: str):
    values = f'id INTEGER PRIMARY KEY AUTOINCREMENT, {columns}'
    return Table(name=table, columns=columns, request=f'CREATE TABLE {table} ({values})')

def create(table: Table, values: str):
    return f'INSERT INTO {table.name} ({table.columns}) VALUES ({values})'

def read(table: Table, condition: str):
    return f'SELECT * FROM {table.name} WHERE {condition}'

def update(table: Table, values:str, condition: str):
    return f'UPDATE {table.name} WHERE {condition} SET {values}'

def delete(table: Table, condition: str):
    return f'DELETE FROM {table.name} WHERE {condition}'
from dataclasses import *
from typing import *
from enum import Enum

@dataclass
class Table:
    name: str
    columns: str
    request: str
    
def search_type(type_):
    if type_ == str:
        return 'VARCHAR'
    elif type_ == int:
        return 'INTEGER'
    elif type_ == bytes:
        return 'BLOB'

def new_table(table:str, data:List[Any]):
    values = 'id INTEGER PRIMARY KEY AUTOINCREMENT, '
    columns = ''
    for i in data:
        if i != data[-1]:
            info = f'{i[0]} {search_type(i[1])}, '
        else:
            info = f'{i[0]} {search_type(i[1])}'
        columns += info
    values += columns
    return Table(name=table, columns=columns, request=f'CREATE TABLE {table} ({values})')

def create(table: Table, values: str):
    return f'INSERT INTO {table.name} ({table.columns}) VALUES ({values})'

def read(table: Table, condition: str):
    return f'SELECT * FROM {table.name} WHERE {condition}'

def update(table: Table, values:str, condition: str):
    return f'UPDATE {table.name} WHERE {condition} SET {values}'

def delete(table: Table, condition: str):
    return f'DELETE FROM {table.name} WHERE {condition}'
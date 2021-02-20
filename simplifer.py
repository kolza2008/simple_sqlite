from typing import Any, Callable, Type, TypeVar

class AdvancedDispatcher:
    def __init__(self, con, cur):
        self.conn = con
        self.cur = cur
        
        self.inits: List[Callable[..., Any]] = [] #list with init methods

    def write(self, func: Callable[..., str]) -> Callable[..., None]:
        "Decorator for create methods for edit or write to sqlite database"
        #print('Database method decorated')
        def db_function(**args):
            data = func(**args)
            self.cur.execute(data)
            self.conn.commit()
        return db_function

    def read(self, func: Callable[..., str]) -> Callable[..., Any]:
        "Decorator for create methods for read data from sqlite database"
        #print('Database method decorated')
        def db_function(*args):
            data = func(*args)
            cur.execute(data)
        return db_function

    def init(self, func: Callable[..., str]) -> Callable[..., str]:
        "Decorator for register init methods"
        #print('New init method')
        self.inits.append(func)
        return func
    
    def start(self) -> None:
        "Method that starts all init methods"
        for i in self.inits:
            try:
                i()
            except:
                pass

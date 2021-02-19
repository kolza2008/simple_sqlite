class AdvancedDispatcher:
    def __init__(self, con, cur):
        self.conn = con
        self.cur = cur
        
        self.inits = [] #list with init methods

    def write(self, func):
        "Decorator for create methods for edit or write to sqlite database"
        #print('Database method decorated')
        def db_function(**args):
            data = func(**args)
            self.cur.execute(data)
            self.conn.commit()
        return db_function

    def read(self, func):
        "Decorator for create methods for read data from sqlite database"
        #print('Database method decorated')
        def db_function(*args):
            data = func(*args)
            cur.execute(data)
        return db_function

    def init(self, func):
        "Decorator for register init methods"
        #print('New init method')
        self.inits.append(func)
        def db_function():
            func()
        return db_function
    
    def start(self):
        "Method that starts all init methods"
        for i in self.inits:
            try:
                i()
            except:
                pass

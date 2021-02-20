from datetime import *

format = '{time}|{func_name} executed'
datetime_format = '%d.%m.%Y %H:%M'

class Logger:
    def __init__(self, type, **args):
        self.type = type
        if type == 'file':
            self.path = args['path']
    def logger_decor(func):
        def logger(**args):
            executed = func(**args)
            log_string = format.format(time=datetime.now().strftime(datetime_format),
                                       func_name = func.__name)
            
            if self.type == 'file':
                with open(self.path, 'w') as f:
                    f.write(log_string)
            elif self.type == 'console':
                print(log_string)
            
            return executed 
            
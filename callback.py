import time

callbacks = {}

def callback_help(callback_func):
    return lambda x: callback_func()

def callback(callback_func):
    def save_callback_decor(main_func):
        def save_callback_func():
            average = main_func()
            callback_func(average)
        return save_callback_func
    return save_callback_decor
        

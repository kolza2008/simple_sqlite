def callback(callback_func):
    def callback_decor(main_func):
        def callback_func():
            main_func()
            callback_func()
        return callback_func
    return callback_decor

def save_callback(callback_func):
    def save_callback_decor(main_func):
        def save_callback_func():
            average = main_func()
            callback_func(average)
        return save_callback_func
    return save_callback_decor
        

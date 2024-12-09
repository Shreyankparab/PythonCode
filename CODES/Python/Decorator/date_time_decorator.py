from datetime import datetime as dt

def date_time(func):
    def wrapper():
        print("Code Initiated...")
        func()
        print("Code Terminated.")
    return wrapper

@date_time

def current_time():
    print("Current time is: ",dt.now().time())

current_time()

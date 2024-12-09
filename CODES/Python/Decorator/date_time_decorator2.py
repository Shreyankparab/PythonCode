from datetime import datetime as dt

def date_time(func):
    def wrapper():
        print("Code Initiated Sucessfully.")
        func()
        print("Code Terminated sucessfully.")
    return wrapper

@date_time

def current_time():
    print("The Current Date is: ",dt.now().date()," and Time is ",dt.now().time())

current_time()

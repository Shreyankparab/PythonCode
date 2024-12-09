from datetime import datetime as dt

def my_dec(func):
    def wrapper():
        print("Code Initiated")
        func()
        print("Code Terminated")
    return wrapper

@my_dec
def greet():
    print("Hi! Hello Everyone...")
greet()

print("=====================================================================")

def date_time(func):
    def wrapper():
        print("Current Time is")
        func()
        print("Code Terminated")
    return wrapper

@my_dec
def current_time():
    print("The current time is ",dt.now())#.date() (For date) .time()(for time) both then nothing
current_time()

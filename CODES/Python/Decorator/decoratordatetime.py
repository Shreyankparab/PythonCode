from datetime import datetime as dt 

def decorator(func):
    def wrapper():
        print("Greeting Initiated at: ",dt.now().time())
        func()
        print("Greeting Completed...",dt.now().time())
    return wrapper

@decorator
def greet():
    print("Hi Hello How are you?")

greet()

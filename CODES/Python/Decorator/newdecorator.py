from datetime import datetime as dt

def my_dec(funct):
    
    def wrapper():
        print("This is Start",dt.now().time())
        funct()
        print("This is End",dt.now().date())
    return wrapper

@my_dec
def New():
    print("Hello There")
New()

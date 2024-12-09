from datetime import datetime as dt

def my_dec(funct):
    def wrapper ():
        print("Start",dt.now().time())
        funct()
        print("End",dt.now().time())
    return wrapper

@my_dec
def demo():
    print("Hello Everyone..")
demo()

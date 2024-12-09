def date_time(funct):
    def wrapper():
        print("Code Initiated")
        funct()
        print("Code Terminated")
    return wrapper

@date_time

def currenttime():
    print("Current Datetime is")

currenttime()

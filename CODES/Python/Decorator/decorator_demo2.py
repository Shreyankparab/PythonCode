def decorator(func):
    def wrapper():
        print("Greeting Initiated...")
        func()
        print("Greeting Completed...")
    return wrapper

@decorator
def greet():
    print("Hi Hello How are you?")

greet()

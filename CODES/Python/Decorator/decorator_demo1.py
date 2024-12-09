def my_deck(func):
    def wrapper():
        print("awdawd")
        func()
        print("dfa")
    return wrapper
@my_deck

def new():
    print("asdfghjk")

new()

def Simple_Generator():
    yield 1
    yield 2
    yield 3

def addition(a,b):
    print(a+b)

result=Simple_Generator()

print(next(result))

print("Outside Yield 1")

print(next(result))

addition(10,20)

print(next(result))

print("Outside Yield 3 ")

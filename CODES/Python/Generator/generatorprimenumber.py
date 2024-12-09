def Simple_Generator():
    yield 1
    yield 2
    yield 3

def prime_number(a):
    for i in range (a,20):
        if i%2==0:
            print(i)
        

result=Simple_Generator()

print(next(result))

print("Outside Yield 1")

print(next(result))

prime_number(10)

print(next(result))

print("Outside Yield 3 ")

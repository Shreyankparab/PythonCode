def primenumber(num):
    if num < 2:
        print("Not a prime number")
        return
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print("Not a prime number")
            return
    print("The number is a prime number")

num = int(input("Enter the Number: "))
primenumber(num)

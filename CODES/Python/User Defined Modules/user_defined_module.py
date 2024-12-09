def addition(a,b):
    print(f"Addition of {a} and {b} is: ",a+b)
def substraction(a,b):
    print(f"Substraction of {a} and {b} is: ",a-b)
def multiplication(a,b):
    print(f"Multiplication of {a} and {b} is: ",a*b)
def division(a,b):
    print(f"Division of {a} and {b} is: ",a/b)
def even_odd(num):
    if num %2==0:
        print(f"The number {num} is a Even Number")
    else:
        print(f"The number {num} is a Odd Number")

def prime_number(num):
    flag=False
    if num == 0 or num == 1:
        print(f"The number {num} is not a prime number ")
    elif num > 1:
        for i in range (2,num):
            if (num%i)==0:
                #print("The number is a Prime number")
                flag=True
                break
        if flag:
            print(f"The number {num} is not a Prime number")
        else:
            print(f"The number {num} is a Prime Number")
    
def is_armstrong(number):
    
    num_str = str(number)
    order = len(num_str)
    sum_of_powers = 0
    
    for digit in num_str:
        sum_of_powers += int(digit) ** order
        if sum_of_powers == number:
            flag= True
        else:
            flag= False

    if flag:
        print(f"The Number {number} is a Armstrong Number ")
    else:
        print(f"The Number {number} is a Armstrong Number ")

        

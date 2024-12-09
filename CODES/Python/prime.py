def primenumber(num):
    if num <2:
        print("Not a prime Number")
        return
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            print("Not a prime Number ")
            return
    print(" prime Number")
        

num=int(input("Enter the Number : "))
primenumber(num)

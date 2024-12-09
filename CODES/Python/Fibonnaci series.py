num=int(input("Enter a Number: "))

if num<=0:
    print("Enter a positive integer ")
elif num==1:
    print("0")
else:
    a,b=0,1
    print(a,b,end=" ")
    for _ in range (2,num):
        c=a+b
        print(c,end=" ")
        a,b=b,c

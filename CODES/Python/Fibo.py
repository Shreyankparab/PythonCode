n=int(input("Emter the number to find the fibbonacci series: "))

if n<=0:
    print("Enter a positive integer")
elif n==1:
    print("0")
else:
    a,b=0,1
    print(a,b, end=" ")
    for _ in range (2,n):
        c=a+b
        print(c,end=" ")
        a,b=b,c

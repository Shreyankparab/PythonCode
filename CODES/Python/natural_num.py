def natural_num(n):
    if n==1:
        return 1
    else:
        return n+natural_num (n-1)

num=input("Enter the Number :")

if num.isdigit() and int(num)>0:
    num=int(num)
    print(f"The Natural Number of {num} is {natural_num(num)}")
else:
    print("SKdhkj")

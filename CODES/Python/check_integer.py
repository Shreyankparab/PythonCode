def check_integer(num):
    if num.isdigit():
        print(f"The number {num} is a integer")
    else:
        print(f"The number {num} is not a integer")

num=input("Enter the number : ")

check_integer(num)

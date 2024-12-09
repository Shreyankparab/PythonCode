class invalid_marks(Exception):
    pass
try:
    num=int(input("Enter your marks: "))

    if num<0 or num >100:
        raise invalid_marks
    else:
        print(f"Your entered marks are {num}")

except invalid_marks:
    print("Enter marks between 1-100")

except Exception as e:
    print("Invalid Input validate the input and reenter the marks")

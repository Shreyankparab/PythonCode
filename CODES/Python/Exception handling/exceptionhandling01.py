class invalid_marks(Exception):
    pass
try:
    marks=int(input("Enter the marks: " ))
    if marks<0 or marks > 100:
        raise invalid_marks
    else:
        print(f"Your marks are {marks}" )
except invalid_marks:
    print("Enter the marks between 0-100 ")

except Exception as e:
    print(f"Exception is {e}")

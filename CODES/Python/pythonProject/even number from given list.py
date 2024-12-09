# number=[1,2,3,4,5,6,7,8,9]
#
# even_number=[num for num in number if num %2 == 0]
# print(even_number)
# ====================================
# fruits=['Apple','Banana','Mango','WaterMelon']
# print(fruits)
# fruits.append('pear')
# print(fruits)
# fruits.sort()
#
# fruits.pop()
#
# print(fruits)
# =====================================
# n = int(input("Enter the number of terms: "))
# fibonacci = [0, 1]
#
# for i in range(2, n):
#     fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
#
# print(fibonacci)
# =================================================
# class ValidAge(Exception):
#     pass
# age=int(input("Enter your age: "))
# try:
#     if age<18:
#         raise ValidAge
#     else:
#         print("You are eligible for voting")
# except ValidAge:
#     print("Your age does not match the criteria for driving licence")
#
# v1=ValidAge()
# ====================================================

# class CheckInteger(Exception):
#     pass
# try:
#     newint = int(input("Enter any number: "))
#     print(newint)
#
# except ValueError:
#     print("The input is Not valid")
# # except CheckInteger as e:
# #     print(e)
#
#
# c1=CheckInteger()
# =======================================================
# Prompt the user for input
# number = int(input("Enter a number: "))
#
# # Reverse the number
# reversed_number = int(str(number)[::-1])
#
# # Find the sum of digits in the reversed number
# digit_sum = sum(int(digit) for digit in str(reversed_number))
#
# # Display results
# print(f"Reversed Number: {reversed_number}")
# print(f"Sum of Digits in Reversed Number: {digit_sum}")

# =======================================================
class NegativeNumber(Exception):
    pass
try:
    number=int(input("Enter any number betn 0-100: "))
    if number<0:
        raise NegativeNumber
    else:
        print("Entered number is valid")

except NegativeNumber:
    print("The Number Entered is less than 0 ")

n1=NegativeNumber()

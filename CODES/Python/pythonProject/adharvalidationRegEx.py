import re


# def Check_adhar(adhar):
#     pattern=r'\d{12}'
#     if re.match(pattern,adhar):
#         print(f"Entered Adhar Number {adhar} is as Valid Adhar Numbar")
#     else:
#         print(f"Entered Adhar Number {adhar} is as InValid Adhar Numbar")
# adhar=input("Enter Your Adhar Number")
# Check_adhar(adhar)




def Check_Pan(pan):
    pattern=r'[A-Z]{5}\d{4}[A-Z]{1}$'
    if re.match(pattern,pan):
        print(f"Entered PAN Number {pan} is as Valid PAN Numbar")
    else:
        print(f"Entered PAN Number {pan} is as InValid PAN Numbar")
pan=input("Enter Your Pan Number.. ")
Check_Pan(pan)



# def Vehicle_Number(v_number):
#     pattern=r'[A-Z]{2}\d{2}[A-Z]{1,2}\d{4}$'
#     if re.match(pattern,v_number):
#         print("Valid Vehicle Number")
#     else:
#         print("InValid Vehicle Number")
# v_number=input("Enter Your Vehicle Number: ")
# Vehicle_Number(v_number)




# def Vehicle_Number(v_number):
#     pattern=r'[A-Z]{2}\d{2}\s\d{11}$'
#     if re.match(pattern,v_number):
#         print("Valid Vehicle License Number")
#     else:
#         print("InValid Vehicle License Number")
# v_number=input("Enter Your Vehicle License Number: ")
# Vehicle_Number(v_number)




# def Password(v_pass):
#     pattern=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*])[a-z A-Z 0-9 !@#$%^&*]{8,}$'
#     if re.match(pattern,v_pass):
#         print("Valid Password")
#     else:
#         print("InValid Password")
# v_pass=input("Enter Your Strong Password: ")
# Password(v_pass)
#
# pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

# def Email_validate(email):
#     pattern = r"^[a-z]+[\._]?[a-z0-9]+[@]\w[\.]\w{2,3}$"
#     if re.match(pattern,email):
#         print("Valid Email Address")
#     else:
#         print("Invalid Email Address")
# email=input("Enter Your Email Id: ")
# Email_validate(email)


# class Student:
#     def __init__(self,name,age,rollno,class_name):
#         self.name=name
#         self.age=age
#         self.rollno=rollno
#         self.class_name=class_name
#     def display(self):
#         print(f"The name of student is {self.name} , having age {self.age}, and is studing in class {self.class_name} ")
#
# s1=Student("shreyank","20",40,"MCA")
# s2=Student("shreyank","20",40,"MCA")
# s3=Student("shreyank","20",40,"MCA")
# s4=Student("shreyank","20",40,"MCA")
# s5=Student("shreyank","20",40,"MCA")
#
# s1.display()
# s2.display()
# s3.display()
# s4.display()


# ==========================================

# class Library:
#     def __init__(self,acc_no,title):
#         self.acc_no=acc_no
#         # self.publisher=publisher
#         self.title=title
#         # self.author=author
#
#     def display(self):
#         print(f"The Account No is {self.acc_no} , title is {self.title} ")
#
#     def compute(self,NoOfDaysLate):
#         days=NoOfDaysLate
#         fine=NoOfDaysLate*10
#         print(f"Your Fine is {fine} of days {days} ")
#     def readdata(self):
#         self.acc_no=int(input("Enter the account no: "))
#         self.title=input("Enter the title: ")
#
#
#
# l1=Library(0,"")
#
# l1.readdata()
# l1.display()
# l1.compute(10)


def filter_words_by_size(input_string, n):
    # Split the input string into words
    words = input_string.split()

    # Create a list of words that are less than size 'n'
    filtered_words = [word for word in words if len(word) < n]

    return filtered_words


# Input string
input_string = "Python programming language has lot of applications in data analytics"

# Size limit 'n'
n = 8

# Get the list of words with length less than 'n'
result = filter_words_by_size(input_string, n)

# Display the result
print("Words with length less than", n, ":", result)

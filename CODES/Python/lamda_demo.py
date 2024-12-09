#addition = lambda a,b:a+b
#substraction = lambda a,b:a-b

addition_substraction = lambda a,b :(a+b,a-b)
a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
add,sub=addition_substraction(a,b)

print("Addition is: ",add," Substraction is: ",sub)

#print("Addition is: ",addition(10,20)," Substraction is: ",substraction(10,20))



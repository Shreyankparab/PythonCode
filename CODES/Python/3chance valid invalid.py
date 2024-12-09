chances = 3

while chances > 0:
    a = input("Enter the String: ")
    
    for i in a:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            print("Invalid String")
            break
    else:
        print("Valid String")
        break

    chances -= 1
    if chances > 0:
        print(f"You have {chances} chance left.")

if chances == 0:
    print("All chances are used")

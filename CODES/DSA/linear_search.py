def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i  
    return -1  

# Define the array
arr = [12, 13, 14, 15, 16, 17, 18, 19]
x = int(input("Enter a number from list [12, 13, 14, 15, 16, 17, 18, 19]: "))
print(arr)

# Function call
result = linear_search(arr, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

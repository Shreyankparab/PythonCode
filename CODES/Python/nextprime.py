num=int(input("Enter a Number"))


for next_num in range(num+1,num*2):
    is_prime=True
    for i in range(2,int(num**0.5)+1):
        if next_num%i==0:
            is_prime=False
            break
    if is_prime:
        print(f"The next prime number after {num}  is {next_num}")
        break
    

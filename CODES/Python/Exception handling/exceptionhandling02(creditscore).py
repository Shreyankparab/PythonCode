class credit_score(Exception):
    pass
try:
    score=int(input("Enter the credit score: " ))
    if score<2000:
        raise credit_score
    else:
        print(f"You are eligible for reddemtion" )
except credit_score:
    print(f"Your Score is {score} which is not sufficient ")

except Exception as e:
    print(f"Exception is {e}")

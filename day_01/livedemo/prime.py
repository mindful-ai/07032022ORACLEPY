# Project A
# To determine if a number is prime or not

def checkprime(n):
    for i in range(2, n):
        if(n % i == 0):
            return False
    return True



# ----------------------------------

print("prime.py: __name__ ---> ", __name__)

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    if(checkprime(n) == True):
        print("The number is prime")
    else:
        print("Then number is not prime")

    

# Program to tell if the result was positive, negative or zero
# after subtraction of two numbers

# input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))


# process
res = a - b

# output
print("-"*50)
print("DIFFERENCE  : ", abs(a - b))
if (res > 0):
    print("The result is positive")
    if (res > 5):
        print("The result is greater than 5")
    else:
        print("The result is lesser than or equal to 5")
elif (res < 0):
    print("The result is negative")
else:
    print("The result is zero")
    

# Accept numbers from the user
# separate the odd and even numbers

# input
nums = []
print("Enter your numbers (negative value to stop): ")
while True:
    n = input("--> ")
    if(n[0] == '-'):
        break
    elif(n.isdigit()):
            nums.append(int(n))
    else:
        print("Enter a number")

print(nums)

# process


odds = []
evens = []
for num in nums:
    if(num % 2 == 0):
        evens.append(num)
    else:
        odds.append(num)
        

# output

print('_'*60)
print('ODDS    : ', odds)
print('EVENS   : ', evens)

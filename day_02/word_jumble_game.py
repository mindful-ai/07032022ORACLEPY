# Develop a word jumble game

# "apples"
# For the user: "pleaps"
# Guess: apples


import random

# Implement the jumble function

def jumble(word):
    return word

# Banner
print('--------------------------------------------------------')
print('                  WORD JUMBLE GAME                      ')
print('--------------------------------------------------------')
print('The computer shows a jumbled word. You need to guess it ')
print('                                       Maximum: 10 words')
print('--------------------------------------------------------')

# User data
username = input("Enter your name: ")

# Get the words from a file: read(), readline(), readlines()
f = open("words.txt", 'r')
words = f.readlines()
f.close()

cleanwords = []
for word in words:
    cleanwords.append(word.strip())

# Shuffle the list
random.shuffle(cleanwords)

# Intialize points
points = 0

# Repeat
for word in cleanwords:
    # Choose a word 
    # Jumble the word
    jw = jumble(word)

    # Present it to the user
    print("Guess this -> ", jw)

    # GEt the user input
    ui = input()

    # Compare and offer points
    if(ui == word):
        points += 1
        print("Correct")
    else:
        print("Incorrect")


# Print the results 
print('--------------------------------------------------------')
print('SCORE : ', points)
if (points > 7):
    print("Excellent")
elif(3 < points < 7):
    print('Good')
else:
    print('Needs improvement')
print('--------------------------------------------------------')

# Log the results in a file: write(), writelines()
f = open("results.txt", 'w')
f.write(username + ':' + str(points) + '\n')
f.close()

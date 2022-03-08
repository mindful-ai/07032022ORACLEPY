import random
class wordjumble:

    def __init__(self, name, age, level=1):
        self.gamer = name 
        self.age = age
        self.level = level
        self.playwords = []
        self.points = 0

    def jumble(self, word): # Elvis Sethi
        rword = random.sample(word,len(word))
        jumbled = ''.join(rword)
        return jumbled


    def banner(self):
        print('--------------------------------------------------------')
        print('                  WORD JUMBLE GAME                      ')
        print('--------------------------------------------------------')
        print('The computer shows a jumbled word. You need to guess it ')
        print('                                       Maximum: 10 words')
        print('--------------------------------------------------------')

    def getwords(self):
        if(self.level == 1):
            f = open("words.txt", 'r')
            words = f.readlines()
            f.close()

            cleanwords = []
            for word in words:
                cleanwords.append(word.strip())

            # Shuffle the list
            random.shuffle(cleanwords)
            self.playwords = cleanwords[:]
        else:
            print('No words for the specified level')

    def play(self):
        print("PLAYER : ", self.gamer, '(', self.age, ')')
        for word in self.playwords:
            # Choose a word 
            # Jumble the word
            jw = self.jumble(word)

            # Present it to the user
            print("Guess this -> ", jw)

            # GEt the user input
            ui = input()

            # Compare and offer points
            if(ui == word):
                self.points += 1
                print("Correct")
            else:
                print("Incorrect")

    def results(self):
        print('--------------------------------------------------------')
        print('SCORE : ', self.points)
        if (self.points > 7):
            print("Excellent")
        elif(3 < self.points < 7):
            print('Good')
        else:
            print('Needs improvement')
        print('--------------------------------------------------------')

    def logresults(self):
        f = open("results.txt", 'a')
        f.write(self.gamer + ' : ' + str(self.age) + " : " + str(self.points) + '\n')
        f.close()

    def run(self):
        self.banner()
        self.getwords()
        self.play()
        self.results()
        self.logresults()

# -----------------------------------------------------------------------

data = [('Purushotham', 40), ('Aditya', 25), ('Anubhav', 25)]

players = []
for item in data:
    players.append(wordjumble(item[0], item[1]))

for player in players:
    player.run()


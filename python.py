import time
import sys

# >> quick presentation of the game <<
print("This is a well-known game called \"Who wants to be a millionaire ? \"")
time.sleep(2)
print(" ")
ready = input("Do you want to be a millionaire ? \n y/n ")
if ready == "y":
    time.sleep(1)
    print(" ")
    print("Let's play that game.")
    time.sleep(2)
else:
    print(" ")
    print("You don't have a choice, sorry.")
    time.sleep(1)

print(" ")
print("Allow me to present the rules.")
time.sleep(2)
print(" ")
print("First rule: \n You only have one guess per question.")
time.sleep(3)
print(" ")
print("Second rule: \n You can use jokers. \n The joker eliminates two wrong answers from the question")
time.sleep(4)
print(" ")
print("Third rule: \n If you think you cannot answer, \n write \"pass\" and the amount won will be yours.")
time.sleep(4)
print(" ")
understand = input("Have you understood the rules ? \n y/n")
if understand == "n":
    print(" ")
    time.sleep(1.5)
    print("Here are the rules again.")
    time.sleep(2)
    print("Allow me to present the rules.")
    print(" ")
    print("First rule: \n You only have one guess per question.")
    print(" ")
    print("Second rule: \n If you think you cannot answer, \n write \"pass\" and the amount won will be yours, but the game will stop")
    print(" ")
    print("Third rule: Only type the letter for your answer.")
else:
    print(" ")
    time.sleep(2)
    print("Let us begin :D \n You start with 0 euros.")



money_amount = 0
only_pass = "See you soon."

class Game:
    def __init__(self, question1, question2, question3, question4, question5):
        self.question1 = question1
        self.question2 = question2
        self.question3 = question3
        self.question4 = question4
        self.question5 = question5
    
    def __repr__(self):
        return "The game has ended and here are your answers. \n question 1: {question1} and the correct answer is b \n question 2: {question2} and the correct answer is c \n question 3: {question3} and the correct answer is a \n question 4: {question4} and the correct answer is c \n question 5: {question5} and the correct answer is d".format(question1=self.question1, question2=self.question2, question3=self.question3, question4=self.question4, question5=self.question5)
    
    def money_amount(self):
        if money_amount == 200000:
            print("You have won 200.000 euros.")
        if money_amount == 400000:
            print("This is the way, you have won 400.000 euros.")
        if money_amount == 600000:
            print("You have 600.000 euros, I'm proud of you.")
        if money_amount == 800000:
            print("You might have reached the million.")
        if money_amount == 1000000:
            print("You are rich, congratulate yourself because you are knowledgeable and rich.")

# >> game starts with questions <<
print(" ")
time.sleep(2)
print("First question")
time.sleep(2)
print(" ")
question1 = input("1) How many countries are there in Europe (2023) ? \n a) 85 \n b) 44 \n c) 52 \n d) 27 \n e) pass \n")
if question1 == "b":
    money_amount += 200000
elif question1 == "e":
    print("You have amassed " + str(money_amount) + " euros. The game is over.")
    print("")
    sys.exit(only_pass)
else:
    money_amount += 0

print("")
time.sleep(2)
print("Second question")
time.sleep(2)
print(" ")
question2 = input("2) In what year was Google created ? \n a) 2004 \n b) 1995 \n c) 1998 \n d) 1980 \n e) pass \n")
if question2 == "c":
    money_amount += 200000
elif question2 == "e":
    print("You have amassed " + str(money_amount) + " euros. The game is over.")
    print("")
    sys.exit(only_pass)
else:
    money_amount += 0

print("")
time.sleep(2)
print("Third question")
time.sleep(2)
print(" ")
question3 = input("3) When was portugal founded ? \n a) 1143 \n b) 1492 \n c) 2001 \n d) 1068 \n e) pass \n")
if question3 == "a":
    money_amount += 200000
elif question3 == "e":
    print("You have amassed " + str(money_amount) + " euros. The game is over.")
    print("")
    sys.exit(only_pass)
else:
    money_amount += 0

print("")
time.sleep(2)
print("Fourth question")
time.sleep(2)
print(" ")
question4 = input("4) How long did Louis XIV reign ? \n a) 52 \n b) 62 \n c) 72 \n d) 82 \n e) pass \n")
if question4 == "c":
    money_amount += 200000
elif question4 == "e":
    print("You have amassed " + str(money_amount) + " euros. The game is over.")
    print("")
    sys.exit(only_pass)
else:
    money_amount += 0

print("")
time.sleep(2)
print("Fifth question")
time.sleep(2)
print(" ")
question5 = input("5) What is Sasuke's brother's name ? \n a) Hatichi \n b) Hitashi \n c) Naruto \n d) Itachi \n e) pass \n")
if question5 == "d":
    money_amount += 200000
elif question5 == "e":
    print("You have amassed " + str(money_amount) + " euros. The game is over.")
    print("")
    sys.exit(only_pass)
else:
    money_amount += 0

game1 = Game(question1,question2,question3,question4,question5)
print(game1)
print("")
print("You have won " + str(money_amount) + " euros")
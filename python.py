import time

# >> quick presentation of the game <<
print("This is a well-known game called \"Who wants to be a millionaire ? \"")
time.sleep(2)
print(" ")
ready = input("Do you want to be a millionaire ? \n y/n ")
if ready == "y":
    time.sleep(1)
    print("Let's play that game.")
    time.sleep(2)
else:
    print("You don't have a choice, sorry.")
    time.sleep(1)

print("Allow me to present the rules.")
time.sleep(2)
print(" ")
print("First rule: \n You only have one guess per question.")
time.sleep(3)
print(" ")
print("Second rule: \n You will have three jokers. \n A joker eliminates two wrong answers from the question")
time.sleep(4)
print(" ")
print("Third rule: \n If you think you cannot answer, \n write \"pass\" and the amount won will be yours.")
time.sleep(4)
print(" ")
understand = input("Have you understood the rules ? \n y/n")
if understand == "n":
    time.sleep(1.5)
    print("Here are the rules again.")
    time.sleep(2)
    print("Allow me to present the rules.")
    print("First rule: \n You only have one guess per question.")
    print("Second rule: \n You will have three jokers. \n A joker eliminates two wrong answers from the question")
    print("Third rule: \n If you think you cannot answer, \n write \"pass\" and the amount won will be yours.")
else:
    time.sleep(2)
    print("Let us begin :D \n You start with 0 euros.")



money_amount = 0
jokers = 3

class Game:
    def __init__(self, question1, question2, question3, question4, question5, question6, question7, question8, question9, question10):
        self.question1 = question1
        self.question2 = question2
        self.question3 = question3
        self.question4 = question4
        self.question5 = question5
        self.question6 = question6
        self.question7 = question7
        self.question8 = question8
        self.question9 = question9
        self.question10 = question10
    
    def __repr__(self):
        return "The game has ended and here are your answers. \n \"question 1: {question1} \" \n \"question 2: {question2} \" \n \"question 3: {question3} \" \n \"question 4: {question4}\" \n \"question 5: {question5} \" \n \"question 6: {question6} \" \n \"question 7: {question7} \" \n \"question 8: {question8} \" \n \"question 9: {question9} \" \n \"question 10: {question10} \" ".format(question1=self.question1, question2=self.question2, question3=self.question3, question4=self.question4, question5=self.question5, question6=self.question6, question7=self.question7, question8=self.question8, question9=self.question9, question10=self.question10)
    
# >> game starts with questions <<
print(" ")
time.sleep(2)
print("First question")
time.sleep(2)
print(" ")
question1 = input("How many countries are there in Europe (2023) ? \n a) 85 \n b) 44 \n c) 52 \n d) 27 \n e) joker \n f) pass \n")
if question1 == "b":
    money_amount += 50000
elif question1 == "joker":
    question1 = input("We eliminate \"a\" and \"c\". You have to choose between \"b\" and \"d\" \n")
    jokers -= 1
    if question1 == "b":
        money_amount += 50000
else:
    money_amount += 0

print(money_amount)
print(jokers)

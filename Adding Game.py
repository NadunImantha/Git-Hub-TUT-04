import random
import os 
ask = input("Do you want to reset the score ? \nEnter y to erase or press any other key to continue.").upper()
if ask == "Y":
    if os.path.exists('Game.txt'):
        with open('Game.txt','w') as file :
            file.write("0")
if os.path.exists('Game.txt'):
    with open('Game.txt','r') as file :
        score = file.read()
else :
    score = "0"
    
score = int(score)
print("Your starting score is ",score)

while True :
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    answer = num1+num2
    question = "what is "+str(num1)+" and "+str(num2)+" added together?"
    #print(num1)
    #print(num2)
    try:
        #guess = int(input("What is the sum value of the above numbers?"))
        guess = input(question)
        if guess == "":
            break
        else :
            print("OOPS Looks like you have entered a string")
        guess = int(guess)
        if guess == answer:
            print("Yeah,you got it.")
            score += 2 

        elif guess != answer :
            print("No the correct answer is ",answer)
            score -= 1
        print("Your score is", score)
    except ValueError :
        #print("OOPS Looks like you have entered a string")
        continue
    
score = str(score)
print("Your new score is ",score)
print("Goodbye Thanks for playing with me")

if os.path.exists('Game.txt'):
    with open('Game.txt','w') as file :
        file.write(score)



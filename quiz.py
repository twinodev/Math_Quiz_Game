#This game will sharpen you brain by going through this simple math quiz
#you will be given an expression to solve it
#all expressions are generated randomly from numbers and operations

#we shall be generating random numbers and operations to use in calculations
#so the random module must be imported first
import random

#the sleep function from time is used at the end when generating results
from time import sleep

#we have created functions to use instead of inbuilt to emphasize concepts grasp
#so they need to be imported here too [* is to import all]
from fomulas import *

print("\nWelcome to Math Quiz Game\n")

#player name is for making the game realistic
player = input("What is your name? :").capitalize()

#playnext is used in our loop to tell if a user wants to continue playing or not
#initially the loop must be true
playnext ="y"
#The whole game is here now
while playnext=="y":
    #choosing complexity level
    print(f"{player}, Please Select a level.")
    print("1.Beginner\n2.Medium\n3.Intermediate\n")
    level = input("Type your level number here👉: ")

    #error handling for non required numbers and characters
    if not level.isdigit():
        print("Please enter a number.")
        exit()
    elif int(level) < 1 or int(level) > 3:
        print("Please enter a Valid number 1-4.")
        exit()
    else:
        #assigning levels different specifications as in operations
        level = int(level)
        if level == 1:
            operators = ["+", "-"]
        elif level == 2:
            operators = ["+","x", "-","/"]
        elif level == 3:
            operators = ["^","+", "-", "x", "/"]

        print("You are doing 10 Questions, 1 Point each.")
        score = 0 #initialising the score

        #loop for the questions
        #we are using 10 questions per round
        for i in range(1, 11):
            #generating random numbers and choosing random operators
            numbers = 10
            num1 = random.randint(0,numbers)
            num2 = random.randint(0,numbers)
            op = random.choice(operators)
            if op == "+":
                answer = add(num1, num2)
            elif op == "-":
                answer = sub(num1, num2)
            elif op == "x":
                answer = mul(num1, num2)
            elif op == "/":
                answer = div(num1, num2)
            elif op == "%":
                answer = mod(num1, num2)
            elif op == "^":
                answer = pow(num1, num2)

            #question format eg. 1+3 = _
            question = f"{num1} {op} {num2} = _"
            #converting answer into a string
            answer = f"{answer}"
            #here question comes, we are using i as our question number
            print(f"\nQuestion {i}:")
            print(question)

            #response from player
            response = input("Answer: ")
            if response == answer:
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect!\nThe correct answer is {answer}")

    print(f"You Finished it.")
    print(f"Evaluating The Questions..")
    sleep(0.5) #applies a 0.5s delay before next line
    print("Collecting your scores..")
    sleep(0.5)
    print("Tallying the scores..")
    sleep(0.5)
    print("Summing the up..")
    sleep(0.5)
    print(f"\nCongratulations! Your score is {score}/10\n")
    sleep(0.5)

    #authorizing the loop
    playnext = input("Do you want to continue? (y/n) : ").lower()

print("Thank you for playing TwinoDev Quizzes!")

#I have done this on my bored day, But I know it means a lot to Us
#Contributions for: Timing each question
#Feel free to contribute to my code as it is opensource
#Follow my Socials and BUY ME COFFEE if you can

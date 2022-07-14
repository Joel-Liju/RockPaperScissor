from random import randint
userpoints, gamepoints = [0,0]
options = {"rock" : 1,"paper" : 2,"scissor" : 3}
print(options)
while True:
    try:
        userChoice = input("Enter your option?\n")
        print(options[userChoice])
        break
    except KeyError:
        print("Something went wrong, Try again")
from random import randint
userpoints, gamepoints = [0,0]
invertedOptions = ["rock","paper","scissor"]
options = {"rock" : 1,"paper" : 2,"scissor" : 0}#each number indicates which things beats it
while True:
    while True:
        try:
            print(options)
            userChoice = input("Enter your option?\n")
            lossingValue = options[userChoice]
            break
        except KeyError:
            print("Something went wrong, Try again")
    print()
    gameChoice = randint(0,2)#0 is rock, 1 is paper, 2 is scissor
    print("The game choose",invertedOptions[gameChoice])
    if gameChoice == lossingValue:
        print("The game wins!")
        gamepoints = gamepoints + 1
    elif (lossingValue-1)%3 == gameChoice:
        print("It is a draw")
    else:
        print("You win!")
        userpoints = userpoints + 1
    print()
    print("Your points : %d , The game points : %d" %(userpoints,gamepoints))
    print()
    
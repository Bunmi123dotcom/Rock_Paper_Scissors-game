import random

c = ['rock', 'paper', 'scissors']

playing = True
while playing is True:
    computer = random.choice(c)
    choice = input(' enter choice ')
    if choice == computer:
        print(' you tie')
    elif choice == "rock":
        if computer == "scissors":
            print(" you win; rock blunts scissors")
        else:
            print(' you lose; paper covers rock')
    elif choice == "scissors":
        if computer == 'rock':
            print(" you lose; rock blunts scissors")
        else:
            print('you win; scissors cuts paper')
    elif choice == "paper":
        if computer == "scissors":
            print(" you lose; scissors cuts paper")
        else:
            print(" you win; paper covers rock")
    elif choice == "quit":
        print(' end of game. thank you')
        break
    else:
        print(' enter a valid choice')
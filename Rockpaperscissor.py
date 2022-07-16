from random import randint

def win():
    print("you win!")
def lose():
    print("you lose!")
def fun():
    while True:
        player_choice = input("Pick your choice:-(Rock,Paper ,Scissors):")
        player_choice.strip()
        random_move = randint(0, 2)
        moves = ['Rock','Paper','Scissors']
        computer_choice =moves [random_move]
        if player_choice == computer_choice:
            print("Draw!")
        elif player_choice == "Rock" and computer_choice == "Scissors":
            win()
        elif player_choice=="Paper" and computer_choice  == "Scissors":
            lose()
        elif  player_choice=="Scissors" and computer_choice == "Paper" :
            win()
        elif player_choice=="Scissors" and computer_choice== "Rock":
            lose()
        elif player_choice == "Paper" and computer_choice == "Rock":
            win()
        elif player_choice == "Paper" and computer_choice == "Rock":
            lose()
        again = input ("Do you want to play again?(y or n)....").strip()
        if again == "n":
            break
fun()
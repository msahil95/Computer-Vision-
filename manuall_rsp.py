
import random
from secrets import choice
 


class RPS:

    def __init__(self) :
        self.select = ["rock", "paper" , "scissors"]
            
    
    def get_computer_choice(self): 
        computer_choice = random.choice(self.select)
        return computer_choice

    def get_user_choice(self):
        user_choice = input ("Please pick rock , paper and scissors: ").lower()
        return user_choice

    def get_winner(self, computer_choice, user_choice):
        if computer_choice == 'paper' and user_choice == 'scissors': #or computer_choice  == 'rock' and user_choice == 'paper' or computer_choice  == 'scissors' and user_choice == 'rock': 
            print(f"Congratulation you won ")
        elif computer_choice == 'rock' and user_choice == 'scissors':
            print("Sorry you lose , try again")
        elif computer_choice  == 'rock' and user_choice == 'paper':
            print(f"Congratulation you won ")
        elif computer_choice == 'scissors' and user_choice == 'paper':
            print("Sorry you lose , try again")
        elif computer_choice  == 'scissors' and user_choice == 'rock':
            print(f"Congratulation you won ")
        elif computer_choice == 'paper' and user_choice == 'rock':
            print("Sorry you lose , try again")
        else:
            print("The game is draw try again to win")
         
            



def play_game():
    
    game = RPS()  
    user_choice = game.get_user_choice()
    computer_choice = game.get_computer_choice()
    print(computer_choice)
    get_winner = game.get_winner(computer_choice,user_choice)


if __name__ == '__main__':
    play_game()
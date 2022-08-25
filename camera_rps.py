import random
import time
import cv2
from keras.models import load_model
import numpy as np

class RPS:
    def __init__(self) :
        self.select = ["rock", "paper" , "scissors", "nothing"]  
        self.user_point = 0
        self.computer_point = 0

    def get_computer_choice(self): 
        self.computer_choice = random.choice(self.select[0:3])
        return self.computer_choice

    def get_prediction(self):
        model = load_model('keras_model.h5')
        self.cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        
        while True: 
            ret, frame = self.cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            cv2.imshow('frame', frame)
            max_index = np.argmax(prediction[0])
            self.user_choice = self.select[max_index]
        
            # Press q to close the window
            print(self.user_choice)
            print(prediction)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        return self.user_choice

    

    def countdown(time_sec):
        while time_sec:
            mins, secs = divmod(time_sec, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            print(timeformat, end='\r')
            time.sleep(1)
            time_sec -= 1

            print("stop")

    countdown(5)     
    
    def get_winner(self, computer_choice,user_choice):
        if computer_choice  == 'paper' and user_choice == 'scissors': #or computer_choice  == 'rock' and user_choice == 'paper' or computer_choice  == 'scissors' and user_choice == 'rock': 
            print(f"Congratulation you won {user_choice}")
            self.user_point +=1
        elif computer_choice == 'rock' and user_choice == 'scissors':
            print("Sorry you lose , try again")
            self.computer_point +=1
        elif computer_choice  == 'rock' and user_choice == 'paper':
            print(f"Congratulation you won {user_choice}")
            self.user_point +=1
        elif computer_choice == 'scissors' and user_choice == 'paper':
            print("Sorry you lose , try again")
            self.computer_point +=1
        elif computer_choice  == 'scissors' and user_choice == 'rock':
            print(f"Congratulation you won {user_choice}")
            self.computer_point +=1
        elif computer_choice == 'paper' and user_choice == 'rock':
            print("Sorry you lose , try again")
            self.computer_point +=1
        else:
            print("The game is draw try again to win")

         
            



def play_game():
    
    game = RPS()  
    round = 0
    while round < 5:
        user_choice = game.get_prediction()
        computer_choice = game.get_computer_choice()
        game.get_winner(user_choice, computer_choice)
        round +=1 
        if game.computer_choice == game.computer_point:
            print(f" Computer wins with {game.get_computer_choice} to {game.get_user_choice}")
        elif game.user_choice == game.user_point:
            print(f" User wins with {game.get_user_choice} to {game.get_computer_choice}")
        else:
            print(f" the score is {game.get_user_choice} and {game.get_computer_choice}")
    

    # After the loop release the cap object
    game.cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

    


if __name__ == '__main__':
    play_game()

    

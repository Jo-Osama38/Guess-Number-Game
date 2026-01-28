from termcolor import colored
from random import randint
import os 
def clear ():
    os.system("clear")
    print('\n'*2)

class Player:
    def __init__(self):
        self.name = ""

    def get_name(self):
        while True:
            print("=-"*20)
            name = input("Your name : (letter Only): ").capitalize().strip()
            if name .isalpha():
                self.name = name
                break
            else:
                print((colored(("Please letter only"), color="red")))

    def get_guess(self):
        while True:
            player_number = input ("Enter Number You Guess :  ").strip()
            if player_number.isdigit():
                return player_number

                
            else:
                print((colored(("You Must Enter Number"),color="red")))

class Menu:
    def start_menu(self):
        print((colored(("          Welcom In Guess Numbr Game"),color="light_cyan")))
        while True:
            choice = input("""1. Start Game
2. Quit Game 
choose 1 or 2 : """)
            if choice in ("1",'2'):
                return choice 
            else :
                print(colored(("     (1,2) Only "),color="red"))
    
    def end_menu(self):
        while True:
            print("-="*20)
            print("=-"*20)
            choice = input("""1. Restart Game 
2. Quit Game 
choose 1 or 2 : """)
            if choice in ("1",'2'):
                return choice 
            else :
                print(colored(("     (1,2) Only "),color="red"))

class Level:
    def __init__(self):
        self.max_num = None
        self.min_num = None
        self.num_attempts = None
        self.name_level = ""
   
    def get_name_level(self):
        while True:
            print("-="*20)
            choice = input("""Choose level you want:
1. Easy 
2. Mid  
3. Hard 
Enter choice (1 or 2 or 3):  """).strip()
            
            if choice in ('1', '2', '3'):
                self.name_level = choice
                break
            else:
                print("-="*20)
                print(colored(('You Must choose 1 or 2 or 3 Only'),color="light_red"))
                print ("-="*20)

           
    def update_information(self):
        if self.name_level == "1":
            self.max_num = 20
            self.min_num = 1
            self.num_attempts = 5
        elif self.name_level == "2":
            self.max_num = 100
            self.min_num = 1
            self.num_attempts = 7
        elif self.name_level == "3":
            self.max_num = 1000
            self.min_num = 400
            self.num_attempts = 10
        print(f"""You Have '{self.num_attempts} attempts'
Max Number '{self.max_num}'
Min Number '{self.min_num}' """)

class Computer:
    def __init__(self):
        self.secret_num = None

    def generate_secret(self, min_num, max_num):
        self.secret_num = randint(min_num ,max_num)
  

class Game:
    def __init__(self):
        self.player = Player()
        self.menu = Menu()
        self.level = Level()
        self.computer = Computer()
        self.attempts_left = 0

    def start_game(self):
        self.player.get_name()
        print(colored(f"Welcom {self.player.name} 👋","magenta"))
        self.level.get_name_level()
        clear()
        self.level.update_information()

        self.attempts_left = self.level.num_attempts
        self.computer.generate_secret(self.level.min_num, self.level.max_num)

        self.play_loop()
        self.end_game()

    def play_loop(self):
        while self.attempts_left > 0:
            guess = int(self.player.get_guess())

            if guess == self.computer.secret_num:
                print(colored("🎉 Congratulations! You guessed it right","green"))
                return


            elif guess < self.level.min_num or guess > self.level.max_num:
                print(colored(f" the Number Must between '{self.level.min_num} and '{self.level.max_num}'","blue"))
                

            elif guess > self.computer.secret_num:
                print("Too high ⬆️")

            else:
                print("Too low ⬇️")

            self.attempts_left -= 1
            print(f"Attempts left: {self.attempts_left}")
        print("-="*20)
        print(colored("    You Lose 😢 ","red"))
        print(f" The Number Was {self.computer.secret_num}")
        print("-="*20)

    def play_game(self):
        choice = self.menu.start_menu()
        if choice == '1':
            self.start_game()
        else:
            self.quit_game()

    def end_game(self):
        choice = self.menu.end_menu()
        if choice == '1':
            self.start_game()
        else:
            self.quit_game()

    def quit_game(self):
        print(colored("I hope you enjoyed it 💛", "yellow"))


game = Game()
game.play_game()

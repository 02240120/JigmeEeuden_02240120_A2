class Main_menu:
    def menu(self):
        print("Select a function (0-5):")
        print("1. Guess Number game")
        print("2. Rock paper scissors game")
        print("3. Trivia Pursuit Game")
        print("4. Pokemon Card Binder Manager")
        print("5. Check Current Overall score")
        print("6. Exit program")
    def __init__(self):
        self.overall_score = {
            'guess_number': 0,
            'rock_paper_scissors': 0,
            'trivia_quiz': 0,
            'pokemon_binder': 0
        }


    def menu_run(self):
        while True:
            self.menu()
            player_choice = int(input("Enter the game you want to play: "))

            if player_choice == 1:
                #run guess the number game
                game = guess_number_game()
                self.overall_score['guess_number'] = game.game_execution()
                print("--------------------------------------------------------------")
            elif player_choice == 2:
                #run rpc
                game2 = rock_paper_scissors()
                self.overall_score['rock_paper_scissors'] = game2.game_execution()
                print("--------------------------------------------------------------")
                
            elif player_choice == 3:
                #run TPG
                game3 = trivia_pursuit_quiz()
                self.overall_score['trivia_quiz'] = game3.quiz_execution()
                print("--------------------------------------------------------------")

            elif player_choice == 4:
                #run  PCBM
                print("")
                print("--------------------------------------------------------------")

            elif player_choice == 5:
                #Check scores
                print("")
                print("--------------------------------------------------------------")

            elif player_choice == 6:
                print("Exiting program !!")
                print("--------------------------------------------------------------")

                break
            else:
                print("Invalid choice! please enter a valid choice")
                print("--------------------------------------------------------------")

#Guess the number
import random
class guess_number_game():
    def __init__(self):
         self.lowest_number = 0
         self.highest_number = 20
    def game_execution(self):
        number_to_be_guessed = random.randint(self.lowest_number, self.highest_number)
        attempt = 0
        valid_numbers = 0
        correct_attempt = 0
        min = 0
        while True:
            try:
                print("Guess a number between 1 and 20: ")
                player_guess = int(input("Your guess is : "))
                if player_guess == number_to_be_guessed:
                    attempt += 1
                    valid_numbers += 1
                    correct_attempt += 1
                    print("Correct!")
                    break
                elif player_guess < number_to_be_guessed:
                    attempt += 1 
                    print("Higher!")
                    continue
                elif player_guess > number_to_be_guessed:
                    attempt += 1 
                    print("Lower!")
                    continue
            except ValueError:
                attempt += 1
                print("Invalid input! \nEnter a valid input!!")
                continue
        score = max(0,attempt-valid_numbers)
        print ("Your score is ",score)
        return score

#Rock, Paper, Scissors
class rock_paper_scissors():
    def __init__(self):
        self.choices = [1,2,3] #1 for rock, 2 for paper, 3 for scissors
        self.win = 0
        self.attempt = 0
    def game_execution(self):
        while True:
            computer_choice = random.choice(self.choices)
            try:
                player_choice = int(input("Enter: \n 1 for rock \n 2 for paper \n 3 for scissors \n 4 to exit \n Your choice: "))
                if player_choice == computer_choice:
                    print("It's a tie!")
                    self.attempt += 1
                elif(player_choice == 1 and computer_choice == 3) or \
                    (player_choice == 2 and computer_choice == 1) or \
                    (player_choice == 3 and computer_choice == 2):
                    print("You win!")
                    self.attempt += 1
                    self.win += 1 

                elif player_choice == 4:
                    break
                else:
                    print("You lost!")
                    self.attempt += 1
            except ValueError:
                print("Invalid choice!")
                continue 
        print(f"You've won {self.win} time against computer in {self.attempt} match")

        

#Trivia Pursuit Quiz Game

class trivia_pursuit_quiz():
    def __init__(self):
        self.score = 0
        self.questions = {
        "Science": [
            { "question": "What is the chemical symbol for gold?",
                "options": ["A. Go", "B. Au", "C. Gd", "D. Ag"],
                "answer": "B" },
           
            { "question": "Which planet is known as the Red Planet?",
                "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
                "answer": "B" } ],
        
        "Mathematics": [
            {
                "question": "Which of the following numbers is not a prime number?",
                "options": ["A. 29", "B. 31", "C. 51", "D. 53"],
                "answer": "C"
            },
            {
                "question": "What is the product of 15*6*4?",
                "options": ["A.360 ", "B.400", "C.350", "D.320"],
                "answer": "A"
            }
        ],
        "Riddle": [
            {
                "question": "I speak with without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?",
                "options": ["A.A Shadow", "B.An echo", "C.A cloud", "D.A Dream"],
                "answer": "B"
            },
            {
                "question": "What has keys but can't open locks?",
                "options": ["A.A piano", "B.A map", "C.A treasure chest", "D.A clock"],
                "answer": "A"
            }
        ]
    }

    def quiz_execution(self):
        print("\nWelcome to Trivia Pursuit Quiz Game!")
        print("Categories available: Riddle,Science, Mathematics,")
        categories = list(self.questions.keys())
        for i in range(0,len(categories)):
            print(f"{i}. {categories[i]}")
            
        try:
            category_choice = int(input("Enter category number: ")) - 1
            selected_category = categories[category_choice]
        except (ValueError, IndexError):
            print("Invalid category selection.")
            return 0
            
        for question in self.questions[selected_category]:
            print("\n" + question['question'])
            for option in question['options']:
                print(option)
                
            user_answer = input("Your answer (A/B/C/D): ").upper()
            if user_answer == question['answer']:
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is {question['answer']}")
                
        print(f"\nYour score: {self.score}/{len(self.questions[selected_category])}")
        return self.score
    
class PokemonBinderManager:
    def play(self):
        print("This feature is implemented in Part B of the assignment.")
        print("Please run the separate Pokemon Binder Manager program.")
            
if __name__ == "__main__":
    menu = Main_menu()
    menu.menu_run()








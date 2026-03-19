##Pokemon Guessing Game

import random #used later to generate random number for result index 
import requests
import sys #used to quit the program when win or loss condition is met
import time #used  later for the time delays

matches = 0
win_counter = 0

def main(matches, win_counter):
    matches = matches + 1
    def whos_that_pokemon():
        try:
            id_number = random.randint(1, 900) #FYI: There are curently 900 different pokemon
            url = "https://pokeapi.co/api/v2"
            response = requests.get(f"{url}/pokemon/{id_number}")
            data = response.json()
            word = data['name']
            print("Starting Match...")
        except requests.exceptions.RequestException:
            print("Network Error. Loading local questions...")
            time.sleep(1)
            print("Starting Match...")
            time.sleep(1)
            print("")
            print("")
            pokemon = ['bulbasaur','garchomp','gengar','umbreon','charizard','mimikyu','lucario','swampert','psyduck','pikachu']
            word = random.choice(pokemon)
        return word

    word = whos_that_pokemon()
    right_counter = 0
    wrong_counter = 0
    previous_choices = []
    
    def game_options():
        if win_counter > 0:
            print("Rounds Won: " + str(win_counter))
        else:
            pass
        
        print("Round: " +  str(matches))
        print("")
        difficulty = input("Choose a difficulty level -> Normal or Hard: ").lower()
        if difficulty in ['normal', 'n', 'norm']:
            difficulty = 'normal'
        elif difficulty in ['hard', 'h']:
            difficulty = 'hard'
        else:
            print("Invalid choice. Please try again.")
            difficulty = game_options()
        return difficulty

    def create_underscore_word(word):
        right_counter = 0
        new_word_underscore = []
        numbers = ["1","2","3","4","5","6","7","8","9","0"]
        for i in  range(len(word)):
            new_word_underscore.append('_')
        for i in range(len(word)):
            if word[i] == '-':
                new_word_underscore[i] = word[i]  
                right_counter += 1
            if word[i] in ' ':
                new_word_underscore[i] = word[i]
                right_counter += 1    
            if word[i] in numbers:
                new_word_underscore[i] = word[i]
                right_counter += 1
        return new_word_underscore, right_counter

    word_underscore, right_counter = create_underscore_word(word)   

    def initial_run(matches):
        if matches == 1:
           
            print('*** Welcome to the Pokémon Guessing Game!! ***')
            
            time.sleep(2) #Pause for 2 seconds for dramatic effect
            print('---------------How to Play:---------------')
            print('Guess which letters are in the word!')
            
            time.sleep(1) #more pausing for dramatic effect
            print("Hint: It's a pokemon!!")
            print("Run out of guesses and it's...")

            over = ['GAME','OVER','FOR','YOU!','---------------------------------------'] 

            # A fun loop to add some character and flair to this game
            for i in over:
                print(i)
                time.sleep(1)
        #### End of presentation elements ####
        return
  
    time.sleep(2)
    print("")
    print("")
    print("")
    initial_run(matches)
    
    difficulty = game_options()
    print("")
    print("")
    print("The pokémon is: ")
    time.sleep(1) 
    print(' '.join(word_underscore)) 

    while True:
        choice = input("Choose a letter: ").lower()
        if len(choice) != 1 or not choice.isalpha():
            print("Invalid choice. Please enter only one letter (a-z).")
            continue
        
        temp = right_counter + 0
        #check previous choices here
        if choice in previous_choices:
            print("Letter already used")
            continue
        previous_choices.append(choice)
        for i in range(len(word)):
            word_letter = word[i]
            if word_letter == 'é':
                word_letter = 'e'
            if choice == word_letter:
                right_counter += 1
                print("Correct!")
                print("")
                word_underscore[i] = word[i]
        print(' '.join(word_underscore))
        if temp == right_counter:
            wrong_counter += 1
            print('Incorrect guess')
            print('')
        if right_counter == len(word):
            print("You win!!")
            win_counter = win_counter + 1
            restart_game(matches, win_counter)
            return
        if difficulty == 'normal' and wrong_counter == 5:
            print('You lose!')
            print("The answer is:" + " " + word)
            restart_game(matches, win_counter)
            return     
        elif difficulty == 'hard' and wrong_counter == 3:
            print('You lose!')
            print("The answer is:" + " " + word)
            restart_game(matches, win_counter)
            return     
            
def restart_game(matches, win_counter): #function to restart game based on user input
    restart = input('Play again? (y/n): ')
    restart = restart.lower()
    if restart in  ['y','yes','yes.']:
        print('*************')
        print('*************')
        print('*************')
        print('*************')
        print('*************')
        
        main(matches, win_counter)
    elif restart in ['n','no','no.']:
        print('Thanks for playing! Goodbye.')
        sys.exit(0)   #Exits program
    else:   
        print('Invalid choice.')
        restart_game(matches, win_counter)
 
if __name__ == "__main__":
    main(matches, win_counter)
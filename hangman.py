##Pokemon Guessing Game

import random #used later to generate random number for result index 
import requests
import sys #used to quit the program when win or loss condition is met
import time #used  later for the time delays

def main():
    def whos_that_pokemon():
        try:
            id_number = random.randint(1, 900) #FYI: There are curently 900 different pokemon
            url = "https://pokeapi.co/api/v2"
            response = requests.get(f"{url}/pokemon/{id_number}")
            data = response.json()
            word = data['name']
        except requests.exceptions.RequestException:
            pokemon = ['greninja','gardevoir','rayquaza','garchomp','sylveon','umbreon','charizard','mimikyu','lucario','gengar','psyduck']
            word = pokemon[(random.randint(0,10))]
        return word

    word = whos_that_pokemon()

    # difficulty = 'normal'
    right_counter = 0
    wrong_counter = 0

    previous_choices = []
    
    
    
    def game_options():
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
        new_word_underscore = []
        for i in  range(len(word)):
            new_word_underscore.append('_')
        for i in range(len(word)):
            if word[i] == '-':
                new_word_underscore[i] = word[i]  
            if word[i] == ' ':
                new_word_underscore[i] = word[i]  
        return new_word_underscore
       
    word_underscore = create_underscore_word(word)
    for i in range(len(word)):
        if word[i] == '-':
            right_counter += 1
        
    #### Superfluous presentation elements - Remove when testing
    print('*** Welcome to the Pokémon Guessing Game!! ***')
    
    # time.sleep(2) #Pause for 2 seconds for dramatic effect
    print('---------------How to Play:---------------')
    print('Guess which letters are in the word!')
    
    # time.sleep(1) #more pausing for dramatic effect
    print("Hint: It's a pokemon!!")
    print("Run out of guesses and it's...")

    over = ['GAME','OVER','FOR','YOU!','---------------------------------------'] 

    # A fun loop to add some character and flair to this game
    for i in over:
        print(i)
        # time.sleep(1)
    #### End of presentation elements ####
    # game_options()
    print("Network Error. Loading local questions...")
    time.sleep(2)
    print("")
    print("")
    print("")
    print("The pokémon is: ") 
    print(' '.join(word_underscore)) 

    #this loop will add 1 to the score, if a blank space is detected in the answer
    for letter in word:  
        if letter == " ": 
            right_counter += 1
        else:
            continue
    difficulty = game_options()
    while True:
        # def game_options():
            # difficulty = input("Choose a difficulty level -> Normal or Hard: ").lower()
            # if difficulty in ['normal', 'n', 'norm']:
            #     difficulty = 'normal'
            #     return difficulty
            # elif difficulty in ['hard', 'h']:
            #     difficulty = 'hard'
            #     # return difficulty
            # else:
            #     print("Invalid choice. Please try again.")
            #     return game_options()

        choice = input("Choose a letter: ").lower()
        if len(choice) != 1 or not choice.isalpha():
            print("Invalid choice. Please enter only one letter (a-z).")
            continue
        
        temp = right_counter + 0
        #check previous choices here
        if len(choice) > 1:
            print("Invalid choice. Only 1 letter per turn")
            continue
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
                word_underscore[i] = word[i]
        print(' '.join(word_underscore))
        if temp == right_counter:
            wrong_counter += 1
            print('Incorrect guess')
            print('')
        if right_counter == len(word):
            print("You win!!")
            restart_game()
            return
        if difficulty == 'normal' and wrong_counter == 5:
            print('You lose!')
            print("The answer is:" + " " + word)
            restart_game()
            return     
        elif difficulty == 'hard' and wrong_counter == 3:
            print('You lose!')
            print("The answer is:" + " " + word)
            restart_game()
            return     
            
def restart_game(): #function to restart game based on user input
    restart = input('Play again? (y/n): ')
    restart = restart.lower()
    if restart in  ['y','yes','yes.']:
        print('*************')
        print('*************')
        print('*************')
        print('*************')
        print('*************')
        main()
    elif restart in ['n','no','no.']:
        print('Thanks for playing! Goodbye.')
        sys.exit(0)   #Exits program
    else:   
        print('Invalid choice.')
        restart_game()
 
if __name__ == "__main__":
    main()
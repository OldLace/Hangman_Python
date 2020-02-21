##The Guessing Game Version 1.3 AKA Hangman - By: Paul Gelot

import random #used later to generate random number for result index 
import sys #used to quit the program when win or loss condition is met
import time #used  later for the time delays

def play_game():
    #All the possible word answers for the game are here in the form of a list 
    result = ['iced coffee','dog','peanut butter','cappuccino','millenials', 'quality control','bird', 'snake','bear','really','blockchain', 'blue','cappuccino','black', 'white', 'orange', 'computer', 'mother-in-law', 'virtual', 'attaché','peanut','netflix', 'résumé', 'good-hearted']
    # result = ['d og','c appuccino','mil lenials', 'b ird', 's nake','be ar','re ally','bloc kchain', 'bl ue','cap puccino','bla ck', 'whi te', 'ora nge', 'com puter', 'mot her-in-law', 'vir tual', 'at taché','pe anut','ne tflix', 'résu mé', 'go od-hearted']


    #Used to generate a random number; the possible indices of the result list
    random_index = random.randint(-1,23)

    # word = 'résumé-resume' #Test word for hyphens
    word = result[random_index]
    right_counter = 0
    wrong_counter = 0

    previous_choices = []

    def create_underscore_word(word):
        new_word_underscore = []
        special_char = 0
        for i in  range(len(word)):
            new_word_underscore.append('_')
        for i in range(len(word)):
            if word[i] == '-':
            #     special_char = 1
                new_word_underscore[i] = word[i]  
            if word[i] == ' ':
                new_word_underscore[i] = word[i]  
        return new_word_underscore
       
    word_underscore = create_underscore_word(word)
    for i in range(len(word)):
        if word[i] == '-':
            right_counter += 1
        
    #### Superfluous presentation elements - Remove when testing
    print('*** Welcome to the Guessing Game!! ***')
    time.sleep(2) #Pause for 2 seconds for dramatic effect
    print('---------------How to Play:---------------')
    print('Guess which letters are in the word!')
    time.sleep(1) #more pausing for dramatic effect
    print("Run out of guesses and it's...")

    over = ['GAME','OVER','FOR','YOU!','---------------------------------------'] 

    # A fun loop to add some character and flair to this game
    for i in over:
        print(i)
        time.sleep(1)
    #### End of presentation elements ####
      
    print("This is your word: ") 
    print(' '.join(word_underscore)) 

    #this loop will add 1 to the score, if a blank space is detected in the answer
    for letter in word:  
        if letter == " ": 
            right_counter += 1
        else:
            continue
    while True: 
        choice = input("Choose a letter: ")
        
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
        if right_counter == len(word):
            print("You win!!")
            restart_game()
            return
        elif wrong_counter == 5:
            print('You lose')
            restart_game()
            return     
            

def restart_game(): #function to restart game based on user input
    restart = input('Play again? ')
    if restart == 'y' or restart == 'Y' or restart == 'yes' or restart == 'Yes':
        print('*************')
        print('*************')
        print('*************')
        print('*************')
        print('*************')
        play_game()
    elif restart == 'n' or restart == 'N' or restart == 'no' or restart == 'No':
        print('Thanks for playing! Goodbye.')
        sys.exit()   #Exits program
    else:   
        print('Invalid choice. Play Again? Yes or No?')
        restart_game()

play_game() 
##The Guessing Game AKA Hangman - By: Paul Gelot

import random #used later to generate random number for result index 
import sys #used to quit the program when win or loss condition is met
import time #used  later for the time delays

def play_game():
    answer_letters = []
    correct_guesses =[]

    status = 5 #Number of guesses player starts game with
    win_state = 0
    right = 0  #Variable for how many correct guesses the player has made

    choice_guesses = []

    #All the possible word answers for the game are here in the form of a list 
    result = ['dog', 'bird', 'snake','bear', 'blue','black', 'white', 'orange', 'computer', 'virtual','peanut','netflix']

    #Used to generate a random number from 0 to 11; the possible indices of the result list
    word_idx = random.randint(-1,11)

    #Needed to get the length of the result element in order to populate it with as many * as the length of the result 
    length_element = [len(i) for i in result[word_idx]]
    correct_guesses = ['_'] * len(result[word_idx])

    print('*** Welcome to the Guessing Game!! ***')
    time.sleep(2) #Pause for 2 seconds for dramatic effect
    print('---------------How to Play:---------------')
    print('Guess which letters are in the word!')
    time.sleep(1)
    print('You begin with', status,'guesses.')
    time.sleep(1)
    print("NOTE: You can type 'status' to see how many chances you have left.")
    time.sleep(2)
    print("Run out of guesses and it's...")

    over = ['GAME','OVER','FOR','YOU!','---------------------------------------'] 
    # A fun loop to add some character and flair to this game
    for i in over:
        print(i)
        time.sleep(1)
    print("This is your word:",correct_guesses)
    for i in result[word_idx]:  #loops through the word at the randomly chosen index
        answer_letters.append(i)   #puts the letters of the word to the answers_letters list
    while win_state == 0:
        if right == len(answer_letters):  #Detects if the number of right guesses is equal to the length of the word
            print('You win!!!!')
            restart_game()
        choice = str(input('Pick a letter: '))
        
        if choice in correct_guesses:  #This loop is used to detect duplicate guesses
            print("Letter already used")
            status = status -1 
            if status <= 0:
                print('***** Game Over *****')
                restart_game()
                
        elif choice in answer_letters:
            print('correct!')
            idx = answer_letters.index(choice)
            correct_guesses.pop(idx)
            correct_guesses.insert(idx,choice) #inserts correct choice into list at the appropriate index
            print(correct_guesses)
            right = right + 1
       
        elif choice == 'status':
            if status > 1:
                print(status, "guesses remaining...")
            else:
                print(status, "guess remaining... no pressure! (._.) ")    
        else:
            print('Incorrect choice!')
            status = status -1 
            if status <= 0:
                print('***** Game Over! Better Luck Next Time... *****') 
                restart_game()

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
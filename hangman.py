# Using the Exercise Branches and Functions, create a simple puzzle game which starts with
# asking user a question. For every question, you should either give user the option to select from
# or let user enter the answer. For each user answer, your game should take the next step
# accordingly using conditions.
# 1. Your game should ask user for input at least five ​times
# 2. Your code should have functions (basically for everything)



#this is the complete word, these are the correct letters that haven't been guessed yet


#the entire alphabet, for guessing purposes

def play():
    choice = input('Pick a letter: ')
    possible_choices = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    answer_letters = ['B','L','U','E']
    correct_guesses =[]
    status = correct_guesses
    status = []
    correct = 'q'

    # for i in answer_letters:
    # if choice == 'status':
    #     print(status)
    for i in answer_letters:
        if choice.upper() == answer_letters:
            print("correct")
            correct = choice.upper()
        else:
            for (idx, val) in enumerate(answer_letters):
          
play()






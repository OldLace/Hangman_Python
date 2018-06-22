# Using the Exercise Branches and Functions, create a simple puzzle game which starts with
# asking user a question. For every question, you should either give user the option to select from
# or let user enter the answer. For each user answer, your game should take the next step
# accordingly using conditions.
# 1. Your game should ask user for input at least five ​times
# 2. Your code should have functions (basically for everything)



#this is the complete word, these are the correct letters that haven't been guessed yet


#the entire alphabet, for guessing purposes
def play():
    choice = str(input('Pick a letter: ')).upper()
    possible_choices = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    answer_letters = ['B','L','U','E']
    correct_guesses =[]
    status = correct_guesses
    status = []
    correct = 'q'
    starter = 0


    if choice in answer_letters:
        print('correct!')
        idx = answer_letters.index(choice)
        correct_guesses.insert(idx,choice)
        print(correct_guesses)
    elif choice == 'status':
        print('status')
    else:
        print('guess is wrong')

play()
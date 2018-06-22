# choice = str(input('Pick a letter: ')).upper()
possible_choices = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
answer_letters = ['B','L','U','E']
correct_guesses =[]
status = correct_guesses
status = []
correct = 'q'
starter = 0

choice_guesses = []

while correct_guesses != answer_letters:
    choice = str(input('Pick a letter: ')).upper()
    if correct_guesses == answer_letters:
        print('Winner, Winner! Chicken Dinner!!')
    elif choice in answer_letters:
        if choice not in correct_guesses:
            print('correct!')
            idx = answer_letters.index(choice)
            correct_guesses.insert(idx,choice)
            print(correct_guesses)
        else:
            print("Letter has been used previously")
    elif choice in correct_guesses:
        print("Letter already used")
    elif choice == 'status':
        print('status')
    else:
        print('guess is wrong')
  



# choice = str(input('Pick a letter: ')).upper()
# if choice in answer_letters:
#     print('correct!')
#     idx = answer_letters.index(choice)
#     correct_guesses.insert(idx,choice)
#     print(correct_guesses)
#     choice = str(input('Pick a letter: ')).upper()
    
# elif choice == 'status':
#     print('status')
# else:
#     print('guess is wrong')



    # def handle_correct():
    #     if choice in answer_letters:
    #         print('correct!')
    #         idx = answer_letters.index(choice)
    #         correct_guesses.insert(idx,choice)
    #         print(correct_guesses)

# playgame()
# choice = str(input('Pick a letter: ')).upper()

import random
import sys

possible_choices = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
answer_letters = []
correct_guesses =[]
# status = correct_guesses
status = 5
correct = 'q'
win_state = 0
right = 0
choice_guesses = []
test_letters = []
# category = input("Please select a category: ")

# for x in range(-1,12)
    

   

result = ['dog', 'bird', 'snake','bear', 'blue','black', 'white', 'orange', 'computer', 'virtual','blockchain','netflix']


word_idx = random.randint(-1,11)
print(word_idx)
length_element = [len(i) for i in result[word_idx]]
print(length_element)
correct_guesses = ['*'] * len(result[word_idx])
# [len(i) for i in result[word_idx]]
# print(length_element)

for i in result[word_idx]:
    answer_letters.append(i)
    print(answer_letters)
# answer_letters.insert(0,result[word_idx][0])
# answer_letters = test_letters
    # while correct_guesses != answer_letters:
while win_state == 0:
    choice = str(input('Pick a letter: '))
    if right == len(answer_letters):
        # win_state = win_state + 1:
        
    # if correct_guesses == answer_letters:
        print('Winner, Winner! Chicken Dinner!!')
        sys.exit()

    if choice in answer_letters:
        # if choice not in correct_guesses:
        print('correct!')
        idx = answer_letters.index(choice)
        # del correct_guesses[idx]
        correct_guesses.pop(idx)
        correct_guesses.insert(idx,choice)
        print(correct_guesses)
        right = right + 1
        
    elif choice in correct_guesses:
        print("Letter already used")
        status = status -1 
    elif choice == 'status':
        print(status, "guesses remaining...")
    else:
        print('Incorrect letter; Pick again')
        status = status -1 
    
import random
#lists
import sys
countries = []
easy_words=[]
medium_words = []
hard_words = []
used_letters= set()
HANGMAN = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
#words

words = open("/home/lazlo/CC/Second week/hangman-python-czlazlo/countries-and-capitals.txt","r")
for lines in words.readlines():
    countries.append(lines.split(" | ")[0])
#ide valahogy meg kellene csinalni hogy lower es upper case is menjen majd a talalgatasnal
#itt definialom az eletet
max_wrong = len(HANGMAN)-1

#wrong guess counter
wrong_guesses = 0
#main loop
for country in countries:
  if len(country) < 6: 
    easy_words.append(country)
  elif len(country) < 9:
    medium_words.append(country)
  elif len(country) > 9:
    hard_words.append(country)

print("Welcome to hangman!")
difficulty = input('Choose a level - 1 , 2  or 3 ')
if (difficulty == "quit"):
  print("Goodbye")
  sys.exit()
print(f"Difficulty level {difficulty}") 
if difficulty == '1':
    max_wrong = 7
    country= random.choice(easy_words)
    dashed_out_word = "_" * len(country)
    print(country)
#Difficulty of word lvl-easy
elif difficulty == '2':
    max_wrong = 5
    country= random.choice(medium_words)
    dashed_out_word = "_" * len(country)
#Difficulty of word lvl-medium
else:
    max_wrong = 3
    country = random.choice(hard_words)
    dashed_out_word = "_" * len(country)
#Difficulty of word lvl- hard

#itt meg jelolom a random szonak a hosszat underscore(_)-ba
#Difficulty for length of words
while wrong_guesses < max_wrong:
    print("Used letters: ", *used_letters)
    print("\n So far, the word is: ", dashed_out_word)
    is_valid_input= False
    while not is_valid_input:
      new_dashed_out_word = ""
      guess= input("\n Please, enter your letter guess:")
      if (guess == "quit"):
        print("Goodbye")
        sys.exit()
      guess= guess.lower()
      if  len(guess) != 1:
        print("please input a letter")
      elif not guess.isalpha():
        print("You can only use letters")
      elif guess in used_letters:
        print("You have already entered this letter")
      else: 
        is_valid_input = True
    used_letters.add(guess)
    if guess not in str(country).lower():
        print(HANGMAN[wrong_guesses])
        guess= guess.lower() 
        print("Sorry, that was incorrect")
    #increase the number of incorrect by 1
        wrong_guesses += 1
    else: 
        print("You have guessed correctly")
        for i in range(len(country)):
          if str(country[i]).lower() == guess:
            new_dashed_out_word += guess
          else:
            new_dashed_out_word += dashed_out_word[i]
        dashed_out_word = new_dashed_out_word
    if wrong_guesses == max_wrong:
      print("You got hanged :(")
      print("The correct word was: ",country)
    if new_dashed_out_word == str(country).lower():
      print("You won!")
      break
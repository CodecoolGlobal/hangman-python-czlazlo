import random
#lists
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
difficulty = input('Choose a level - 1 (7 lives, easy words), 2 (5 lives, medium words ) or 3 (3 hard words)')
print(f"Difficulty level {difficulty}") 
if difficulty == '1':
    max_wrong = 7
    country= random.choice(easy_words)
    dashed_out_word = "_" * len(country)
    print(country)
    print(dashed_out_word)
#Difficulty of word lvl-easy
elif difficulty == '2':
    max_wrong = 5
    country= random.choice(medium_words)
    dashed_out_word = "_" * len(country)
    print(country)
    print(dashed_out_word)
#Difficulty of word lvl-medium
else:
    max_wrong = 3
    country = random.choice(hard_words)
    dashed_out_word = "_" * len(country)
    print(country)
    print(dashed_out_word)
#Difficulty of word lvl- hard


#itt meg jelolom a random szonak a hosszat underscore(_)-ba
#Difficulty for length of words
while wrong_guesses < max_wrong:
    print("Used letters: ", used_letters)
    print("so far, the word is: ", dashed_out_word)
    guess= input("enter your letter guess:")
    used_letters.add(guess)
    if guess not in country:
        print(HANGMAN[wrong_guesses])
        guess= guess.upper() 
        print("Sorry, that was incorrect")
    #increase the number of incorrect by 1
        wrong_guesses += 1

    else: 
        print("You have guessed correctly")
        new_dashed_out_word = ""
        for i in range(len(country)):
          if country[i] == guess:
            new_dashed_out_word += guess
          else:
            new_dashed_out_word += dashed_out_word[i]
        dashed_out_word = new_dashed_out_word

                                    #add new guessed letter to list of guessed letters
     
     #give a new version of the word with mixed letters and dashe
#check if letter was already used


if guess in used_letters:
    print("You have already guessed that letter", guess)
    guess = input("Enter your letter guess:")
    guess = guess.lower()
#add new guessed letter to list of guessed letters
    used_letters.append(guess)

#end game
else:
    print("You get to live")
    wrong_guesses == max_wrong
    print(HANGMAN[wrong_guesses])
    print("*Gets hanged*")
    print("The correct word was",country)
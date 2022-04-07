#imports
import random



#constants
HANGMAN_PICS = ['''
  3.   +---+
  4.       |
  5.       |
  6.       |
  7.      ===''', '''
  8.   +---+
  9.   O   |
 10.       |
 11.       |
 12.      ===''', '''
 13.   +---+
 14.   O   |
 15.   |   |
 16.       |
 17.      ===''', '''
 18.   +---+
 19.   O   |
 20.  /|   |
 21.       |
 22.      ===''', '''
 23.   +---+
 24.   O   |
 25.  /|\  |
 26.       |
 27.      ===''', '''
 28.   +---+
 29.   O   |
 30.  /|\  |
 31.  /    |
 32.      ===''', '''
 33.   +---+
 34.   O   |
 35.  /|\  |
 36.  / \  |
 37.      ===''']

words = open("/home/lazlo/CC/Second week/hangman-python-czlazlo/countries-and-capitals.txt","r")
words.readlines()

max_wrong = len(HANGMAN_PICS) - 1

#pick a word
words = random.choice(words)
print(words)


#dashes for each letter in a word
current_guess = "-"*len(words)

#wrong guess counter
wrong_guesses = 0

#used letters tracker
used_letters = []

#main loop
print("welcome to hell")
difficulty = input("Select difficulty level:1/2/3")
print("Difficulty level {difficulty}")

while wrong_guesses < max_wrong:
    if current_guess not in words:
        print([wrong_guesses-1])
        print("Used letters: ", used_letters)
        print("so far, the word is: ", current_guess)

guess= input("enter your letter guess:")
guess= guess.lower()

 #check if letter was already used
while guess in used_letters:
      print("You have already guessed that letter", guess)
      guess = input("Enter your letter guess:")
      guess = guess.lower()

#add new guessed letter to list of guessed letters
used_letters.append(guess)

#check guess
if guess in words:
    print("You have guessed correctly")

     
     #give a new version of the word with mixed letters and dashes
    new_current_guess = ""
    for letter in range(len(words)):
        if guess == words[letter]:
            new_current_guess += guess
        else:
            new_current_guess += current_guess[letter]

    current_guess = new_current_guess
else:
    print("Sorry, you lose your life now")

#Eng the game
if wrong_guesses == max_wrong:
    print(HANGMAN_PICS[wrong_guesses])
    print("*Gets hanged*")
    print("The correct word was",words)

else:
    print("You get to live")

import random
import string
from words import words

def getValidWord(wordsList):
  word = random.choice(wordsList)
  while '-' in word or ' ' in word:
    word = random.choice(wordsList)

  return word.upper()
    
def hangman():
  wordToGuest = getValidWord(words)
  wordLetters = set(wordToGuest) # letters in the word
  alphabet = set(string.ascii_uppercase)
  usedLetters = set() # what the user has guest
  playAgain = False

  while len(wordLetters) > 0 | playAgain:
    if len(wordLetters) > 1: print('You have used these letters => ', ' '.join(usedLetters))

    # what current word is (ie W - R D)
    wordList = [letter if letter in usedLetters else '-' for letter in wordToGuest]
    print('Current word:', ' '.join(wordList))

    userLetter = input('❓ Guest a letter: ').upper()
    if userLetter in alphabet - usedLetters:
      usedLetters.add(userLetter)
      if userLetter in wordLetters:
        wordLetters.remove(userLetter)
    elif userLetter in usedLetters:
      print('You have already used that character. Tyr again')

  print('🎉 Congratulations! The word was: ' + wordToGuest)

hangman()

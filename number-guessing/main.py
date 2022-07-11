import random

def guess(limit):
  randomNumber = random.randint(1, limit)
  userNumber = 0
  times = 0
  while (userNumber != randomNumber):
    times += 1
    userNumber = int(input(f'-❓Guess a number between 1 and {limit}: '))
    if(userNumber > randomNumber):
      print('Lower')
    if(userNumber < randomNumber):
      print('Higher')
    if(userNumber == randomNumber):
      print(f'🥳 Congratulation you guess the number in {times} times!')

guess(10)

import random

typeofcard = ["heart", "diamond", "club", "spade"]
numberoncard = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
usedcard = []
playercard = []
computercard = []
isplayer = True

def clear():
  print('\033[H\033[J', end='')
  
#Generate a random card
def randomcard():
  global isplayer
  while True:
    cardtype = random.choice(typeofcard)
    cardnum = random.choice(numberoncard)
    try:
      value = int(cardnum)
    except:
      if cardnum == "A" and isplayer:
        while True:
          print("------------------------------------$$$$$$$$$$$$$-------------------------------------------")
          print("You had draw an Ace card.")
          uservalue = int(input("Choose the value you want for your card (either 1 or 11): "))
          if uservalue == 1 or uservalue == 11:
            value = uservalue
            break
          print("Invalid value!!!")
      elif cardnum == "A" and not isplayer:
        if computervalue() <= 10:
          value = 11
        else:
          value = 1

      else:
        value = 10
    return [cardtype, cardnum, value]

#check if the card is used or not and return a card
def returncard():
  while True:
    card1 = randomcard()
    cards = [card1[0], card1[1]]
    for items in usedcard:
      if cards == items:
        continue
    usedcard.append(cards)
    return card1


#Give the player an access to draw a card 
def drawcard():
  while True:
    print("")
    userinput = input("Draw a card by typing \"draw\" or type \"no\" to not draw a card: ")
    if userinput.lower().strip() == "draw":
      returncard()
      print(playercard)
      continue
    elif userinput.lower().strip() == "no":
      return("Done!")

#Start game by giving each player a card
def game(x, y):
  global isplayer
  for i in range(4):
    x.append(returncard())
    isplayer = False
    y.append(returncard())
    isplayer = True

#Computer will pick a value for "A" card
def computervalue():
  value = 0
  for i in computercard:
    value += i[2]
  return value

'''
#Calculate computer card total value
def computertotalvalue():
  totalvalue = 0
  for
  return 

#Calculate player card total value
def playertotalvalue():
  return 

#Dtermine the winner
def winner(x, y):
  if x > y:
    return "Computer win!"
  elif x == y:
    return "TIE!"
  elif x < y:
    return "Player win!"
'''

#Instruction for the player
def instructions():
  while True:
    enter = input("Type \"yes\" to see the instructions or \"no\" to skip: ")
    if enter.lower().strip() == "yes":
      print("----------------------------------------------------------------------------------------------------")
      print("Here is the instructions: ")
      print("The type of cards in this game does not matter. What matter is the value of the card you holding.")
      print("Here is the convert value for your card: ")
      print("Card num          Value")
      print("    2               2")
      print("    3               3")
      print("    4               4")
      print("    5               5")
      print("    6               6")
      print("    7               7")
      print("    8               8")
      print("    9               9")
      print("    10             10")
      print("    J              10")
      print("    Q              10")
      print("    K              10")
      print("    A              either 1 or 11 based on your choice")
      print("----------------------------------------------------------------------------------------------------")
      print("Good luck and have fun!!!")
      print("----------------------------------------------------------------------------------------------------")
      break
    elif enter.lower().strip() == "no":
      print("Good luck and have fun!!!")
      print("----------------------------------------------------------------------------------------------------")
      break

#Rules for the player
def rules():
  while True:
    print("-------------------------------------------$$BLACKJACK$$------------------------------------------------")
    print("Welcome to our table!!!")
    print("This is a program where you can play with a computer is a house for the game!")
    print("Please read the instruction if you never play before!")
    enter = input("Type \"yes\" to see the rules or \"no\" to skip: ")
    if enter.lower().strip() == "yes":
      print ("--------------------------------------------------------------------------------------------------------")
      print("Blackjack rules:")
      print("Rule 1: Start with 2 cards each card will have different value and your job is to get your total value to be as near as possible to 21. ")
      print("Rule 2: If your total value reach higher than 21, you LOSE!!!")
      print("Rule 3: When no one draw any card anymore, the one that has the higher value than the house WIN.")
      print("--------------------------------------------------------------------------------------------------------")
      instructions()
      break
    elif enter.lower().strip() == "no":
      instructions()
      break


#Start program
rules()
game(playercard, computercard)
print("This is computer card: " + str(computercard))




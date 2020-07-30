# Handle Imports
import colorama as cr
from colorama import Fore, Back, Style
import time
import os
import random
cr.init(autoreset = True)

def DrawTable(B, H):
  global numberAssist
  y = 0
  for k in (len(B) * "."):
    row = ""
    x = 0
    for l in "....":
      if(B[y][x] == 0):
        row = row + Fore.RESET + "◯ "
      elif(B[y][x] == 1):
        row = row + Fore.RED + "⬤ "
      elif(B[y][x] == 2):
        row = row + Fore.GREEN + "⬤ "
      elif(B[y][x] == 3):
        row = row + Fore.BLUE + "⬤ "
      elif(B[y][x] == 4):
        row = row + Fore.CYAN + "⬤ "
      elif(B[y][x] == 5):
        row = row + Fore.MAGENTA + "⬤ "
      elif(B[y][x] == 6):
        row = row + Fore.YELLOW + "⬤ "
      row = row + "   "
      x = x + 1
    px = 0
    for m in "....":
      if(H[y][px] == 1):
        row = row + Fore.BLACK + "🞉 "
      elif(H[y][px] == 2):
        row = row + Fore.WHITE + "🞉 "
      else:
        row = row + "  "
      px = px + 1
    if(numberAssist == True and B[y] != [0, 0, 0, 0]):
      row = row + Fore.RESET + "      " + str(B[y][0]) + " , " + str(B[y][1]) + " , " + str(B[y][2]) + " , " + str(B[y][3])
    print(row)
    y = y + 1

  




def SinglePlayer():
  os.system('cls')
  print()
  print(" .d8888b.  d8b                   888               8888888b.  888")                                
  print("d88P  Y88b Y8P                   888               888   Y88b 888")                                
  print("Y88b.                            888               888    888 888")                                 
  print("  Y888b.   888 88888b.   .d88b.  888  .d88b.       888   d88P 888  8888b.  888  888  .d88b.  888d888 ")
  print("     Y88b. 888 888  88b d88P 88b 888 d8P  Y8b      8888888P   888      88b 888  888 d8P  Y8b 888P") 
  print("       888 888 888  888 888  888 888 88888888      888        888 .d888888 888  888 88888888 888")  
  print("Y88b  d88P 888 888  888 Y88b 888 888 Y8b.          888        888 888  888 Y88b 888 Y8b.     888")  
  print("  Y8888P   888 888  888   Y88888 888   Y8888       888        888  Y888888   Y88888   Y8888  888")  
  print("                             888                                                888")          
  print("                        Y8b d88P                                           Y8b d88P")           
  print("                          Y88P                                               Y88P  ")
  print()
  print("You have chosen " + Fore.BLUE + " single player mode")
  print("In this mode, you will be facing off against a computer")
  print("The computer will be the " + Fore.YELLOW + "Codemaker" + Fore.RESET + ", and you are the " + Fore.YELLOW + "Codebreaker")
  print()
  valid = 0
  while(valid == 0):
    try:
      rounds = int(input("Enter how many complete rounds you wish to play > "))
      valid = 1
    except ValueError:
      print("Enter a " + Fore.RED + "number" + Fore.RESET + " value")
    print()
  print()
  os.system('cls')
  print()
  roundCounter = 1
  playerWins = 0
  computerWins = 0
  # Symbols > ◯⬤🞉
  # Main Peg Colours 0 = none, 1 = red, 2 = green, 3 = blue, 4 = cyan, 5 = magenta, 6 = yellow
  # Hint Peg Colours 0 = none, 1 = black, 2 = white
  for i in (rounds * "."):
    B = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
    H = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
    Answer = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
    Colours = [Fore.RED + "⬤ ", Fore.GREEN + "⬤ ", Fore.BLUE + "⬤ ", Fore.CYAN + "⬤ ", Fore.MAGENTA + "⬤ ", Fore.YELLOW + "⬤ ", ]
    winState = 0
    turnsleft = 12
    print()
    print()
    print(Fore.GREEN + "ROUND " + str(roundCounter))
    print("You are the " + Fore.YELLOW + " Codebreaker")
    roundCounter = roundCounter + 1
    while(turnsleft > 0):
      print()
      print()
      DrawTable(B, H)
      print("_________________")
      print("| ? | ? | ? | ? |")
      print("-----------------")
      print()
      print()
      attempt = [0,0,0,0]
      print("1 > " + Fore.RED + "⬤" + Fore.RESET + "   ,   2 > " + Fore.GREEN + "⬤")
      print("3 > " + Fore.BLUE + "⬤" + Fore.RESET + "   ,   4 > " + Fore.CYAN + "⬤")
      print("5 > " + Fore.MAGENTA + "⬤" + Fore.RESET + "   ,   6 > " + Fore.YELLOW + "⬤")
      print()
      entryComplete = 0
      while(entryComplete == 0):
        index = 0
        sequence = ""
        for j in "....":
          valid = 0
          while(valid == 0):
            try:
              entry = int(input("Enter the number for space " + str(index) + " > "))
              if(entry < 7 and entry > 0):
                valid = 1
                attempt[index] = entry
                sequence = sequence + Colours[entry - 1] + " "
                print(sequence)
              else:
                print("Enter a number between " + Fore.RED + "1 and 6")
            except ValueError:
              print("Enter a " + Fore.RED + "number" + Fore.RESET + " value")
          index = index + 1
        confirm = input("Confirm Selection? (y/n) > ")
        if(confirm == "y" or confirm == "Y"):
          entryComplete = 1
        else:
          print()
      print()
      B[12 - turnsleft] = attempt
      pegs = [0, 0, 0, 0]
      attemptClone = [attempt[0], attempt[1], attempt[2], attempt[3]]
      answerClone = [Answer[0], Answer[1], Answer[2], Answer[3]]
      insertionPoint = 0
      count = 0
      for j in "....":
        if(attemptClone[count] == Answer[count]):
          pegs[insertionPoint] = 1
          attemptClone[count] = 0
          answerClone[count] = 0
          insertionPoint = insertionPoint + 1
        count = count + 1
      count = 0
      for j in "....":
        if(attemptClone[count] != 0 and attemptClone[count] in answerClone):
          pegs[insertionPoint] = 2
          wipePoint = answerClone.index(attemptClone[count])
          answerClone[wipePoint] = 0
          attemptClone[count] = 0
          insertionPoint = insertionPoint + 1
        count = count + 1
      H[12 - turnsleft] = pegs
      if(pegs == [1, 1, 1, 1]):
        turnsleft = 0
        winState = 1
      else:
        turnsleft = turnsleft - 1
      print() 
      print()
    if(winState == 0):
      DrawTable(B, H)
      print("_________________")
      print("| " + Colours[Answer[0] - 1] + Fore.RESET + "| " + Colours[Answer[1] - 1] + Fore.RESET + "| " + Colours[Answer[2] - 1] + Fore.RESET + "| " + Colours[Answer[3] - 1] + Fore.RESET + "|")
      print("-----------------")
      print()
      print()
      print(Fore.RED + "GAME OVER" + Fore.RESET + " - No Turns Left")
      computerWins = computerWins + 1
    else:
      DrawTable(B, H)
      print("_________________")
      print("| " + Colours[Answer[0] - 1] + Fore.RESET + "| " + Colours[Answer[1] - 1] + Fore.RESET + "| " + Colours[Answer[2] - 1] + Fore.RESET + "| " + Colours[Answer[3] - 1] + Fore.RESET + "|")
      print("-----------------")
      print()
      print()
      print(Fore.GREEN + "YOU WIN" + Fore.RESET + " - You got the right answer!")
      playerWins = playerWins + 1
    print()
    stop = input("Press Enter To Continue")
  print()
  print()
  print(Fore.CYAN + "FINAL SCORES : ")
  print("Player Wins > " + str(playerWins))
  print("Computer Wins > " + str(computerWins))
  if(playerWins == computerWins):
    print("It's a " + Fore.YELLOW + "DRAW")
  elif(playerWins > computerWins):
    print(Fore.GREEN + "YOU WIN")
  else:
    print(Fore.RED + "THE COMPUTER WINS")
  print()
  stop = input("Press Enter To Continue")





def TwoPlayer():
  os.system('cls')
  print()
  print("88888888888                          8888888b.  888                                    ")
  print("    888                              888   Y88b 888                                    ")
  print("    888                              888    888 888                                    ")
  print("    888  888  888  888  .d88b.       888   d88P 888  8888b.  888  888  .d88b.  888d888 ")
  print("    888  888  888  888 d88  88b      8888888P   888      88b 888  888 d8P  Y8b 888P    ")
  print("    888  888  888  888 888  888      888        888 .d888888 888  888 88888888 888     ")
  print("    888  Y88b 888 d88P Y88..88P      888        888 888  888 Y88b 888 Y8b.     888     ")
  print("    888    Y8888888P     Y88P        888        888  Y888888   Y88888   Y8888  888     ")
  print("                                                                  888                  ")
  print("                                                             Y8b d88P                  ")
  print("                                                               Y88P ")
  print()
  print("You have chosen " + Fore.BLUE + " two player mode")
  print("This mode requires 2 people to play, and operates much in the style of traditional Mastermind > where your points are determined by the number of turns it takes for the other player to crack your code.")
  print("You will take turns being " + Fore.YELLOW + "Codemaker" + Fore.RESET + " and " + Fore.YELLOW + "Codebreaker")
  print()
  user1Name = input("Enter the name of Player 1 > ")
  user2Name = input("Enter the name of Player 2 > ")
  print()
  valid = 0
  while(valid == 0):
    try:
      rounds = int(input("Enter how many complete rounds you wish to play (A complete round consists of 2 rounds, in which both users play as " + Fore.YELLOW + "Codemaker" + Fore.RESET + ") > "))
      valid = 1
    except ValueError:
      print("Enter a " + Fore.RED + "number" + Fore.RESET + " value")
    print()
  print()
  os.system('cls')
  print()
  roundCounter = 1
  user1Points = 0
  user2Points = 0
  codemaker = 1
  # Symbols > ◯⬤🞉
  # Main Peg Colours 0 = none, 1 = red, 2 = green, 3 = blue, 4 = cyan, 5 = magenta, 6 = yellow
  # Hint Peg Colours 0 = none, 1 = black, 2 = white
  for i in (rounds * 2 * "."):
    B = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
    H = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
    Colours = [Fore.RED + "⬤ ", Fore.GREEN + "⬤ ", Fore.BLUE + "⬤ ", Fore.CYAN + "⬤ ", Fore.MAGENTA + "⬤ ", Fore.YELLOW + "⬤ ", ]
    winState = 0
    turnsleft = 12
    print()
    print()
    print(Fore.GREEN + "ROUND " + str(roundCounter))
    if(codemaker == 1):
      print(user1Name + " is the " + Fore.YELLOW + " Codemaker")
    else:
      print(user2Name + " is the " + Fore.YELLOW + " Codemaker")
    print()
    print(Fore.YELLOW + "Codemaker's " + Fore.RESET + "turn.")
    print()
    print("1 > " + Fore.RED + "⬤" + Fore.RESET + "   ,   2 > " + Fore.GREEN + "⬤")
    print("3 > " + Fore.BLUE + "⬤" + Fore.RESET + "   ,   4 > " + Fore.CYAN + "⬤")
    print("5 > " + Fore.MAGENTA + "⬤" + Fore.RESET + "   ,   6 > " + Fore.YELLOW + "⬤")
    print()
    Answer = [0,0,0,0]
    entryComplete = 0
    while(entryComplete == 0):
      index = 0
      sequence = ""
      for j in "....":
        valid = 0
        while(valid == 0):
          try:
            entry = int(input("Enter the number for space " + str(index) + " > "))
            if(entry < 7 and entry > 0):
              valid = 1
              Answer[index] = entry
              sequence = sequence + Colours[entry - 1] + " "
              print(sequence)
            else:
              print("Enter a number between " + Fore.RED + "1 and 6")
          except ValueError:
            print("Enter a " + Fore.RED + "number" + Fore.RESET + " value")
        index = index + 1
      confirm = input("Confirm Selection? (y/n) > ")
      if(confirm == "y" or confirm == "Y"):
        entryComplete = 1
      else:
        print()
    print("You are the " + Fore.YELLOW + " Codebreaker")
    roundCounter = roundCounter + 1
    turn = 2
    while(turnsleft > 0):
      if(turn == 2):
        for m in ".........":
          print()
        os.system('cls')
        print()
        if(codemaker == 1):
          print(Fore.YELLOW + user2Name + "'s " + Fore.RESET + "turn.")
        else:
          print(Fore.YELLOW + user1Name + "'s " + Fore.RESET + "turn.")
        print()
        print()
        DrawTable(B, H)
        print("_________________")
        print("| ? | ? | ? | ? |")
        print("-----------------")
        print()
        print()
        attempt = [0,0,0,0]
        print("1 > " + Fore.RED + "⬤" + Fore.RESET + "   ,   2 > " + Fore.GREEN + "⬤")
        print("3 > " + Fore.BLUE + "⬤" + Fore.RESET + "   ,   4 > " + Fore.CYAN + "⬤")
        print("5 > " + Fore.MAGENTA + "⬤" + Fore.RESET + "   ,   6 > " + Fore.YELLOW + "⬤")
        print()
        entryComplete = 0
        while(entryComplete == 0):
          index = 0
          sequence = ""
          for j in "....":
            valid = 0
            while(valid == 0):
              try:
                entry = int(input("Enter the number for space " + str(index) + " > "))
                if(entry < 7 and entry > 0):
                  valid = 1
                  attempt[index] = entry
                  sequence = sequence + Colours[entry - 1] + " "
                  print(sequence)
                else:
                  print("Enter a number between " + Fore.RED + "1 and 6")
              except ValueError:
                print("Enter a " + Fore.RED + "number" + Fore.RESET + " value")
            index = index + 1
          confirm = input("Confirm Selection? (y/n) > ")
          if(confirm == "y" or confirm == "Y"):
            entryComplete = 1
          else:
            print()
        print()
        B[12 - turnsleft] = attempt
        turn = 1
      else:
        for m in ".........":
          print()
        os.system('cls')
        print()
        if(codemaker == 1):
          print(Fore.YELLOW + user1Name + "'s " + Fore.RESET + "turn.")
        else:
          print(Fore.YELLOW + user2Name + "'s " + Fore.RESET + "turn.")
        print()
        stop = input("Press enter once only the " + Fore.YELLOW + " Codemaker" + Fore.RESET + " can see the screen.")
        print()
        print()
        print()
        pegs = [0, 0, 0, 0]
        pegColours = [" ", Fore.BLACK + "🞉 ", Fore.WHITE + "🞉 "]
        entryComplete = 0
        print("Answer              > " + Colours[Answer[0] - 1] + " " + Colours[Answer[1] - 1] + " " + Colours[Answer[2] - 1] + " " + Colours[Answer[3] - 1])
        print()
        print(Fore.YELLOW + "Codebreaker's" + Fore.RESET + " guess > " + Colours[B[12 - turnsleft][0] - 1] + " " + Colours[B[12 - turnsleft][1] - 1] + " " + Colours[B[12 - turnsleft][2] - 1] + " " + Colours[B[12 - turnsleft][3] - 1])
        print()
        print()
        print("0 > No Peg")
        print("1 > " + Fore.BLACK + "🞉" + Fore.RESET + "   (Correctly coloured peg in the right place)")
        print("2 > " + Fore.WHITE + "🞉" + Fore.RESET + "   (Correctly coloured peg in the wrong place)")
        while(entryComplete == 0):
          index = 0
          sequence = ""
          for j in "....":
            valid = 0
            while(valid == 0):
              try:
                entry = int(input("Enter the number for space " + str(index) + " > "))
                if(entry < 3 and entry > -1):
                  valid = 1
                  pegs[index] = entry
                  sequence = sequence + pegColours[entry] + " "
                  print(sequence)
                else:
                  print("Enter a number between " + Fore.RED + "0 and 2")
              except ValueError:
                print("Enter a " + Fore.RED + "number" + Fore.RESET + " value")
            index = index + 1
          confirm = input("Confirm Selection? (y/n) > ")
          if(confirm == "y" or confirm == "Y"):
            entryComplete = 1
          else:
            print()
        H[12 - turnsleft] = pegs
        if(pegs == [1, 1, 1, 1]):
          turnsleft = 0
          winState = 1
        else:
          turnsleft = turnsleft - 1
          turn = 2
        if(codemaker == 1):
          user1Points = user1Points + 1
        else:
          user2Points = user2Points + 1
        print() 
        print()
    if(winState == 0):
      DrawTable(B, H)
      print("_________________")
      print("| " + Colours[Answer[0] - 1] + Fore.RESET + "| " + Colours[Answer[1] - 1] + Fore.RESET + "| " + Colours[Answer[2] - 1] + Fore.RESET + "| " + Colours[Answer[3] - 1] + Fore.RESET + "|")
      print("-----------------")
      print()
      print()
      print(Fore.YELLOW + "Codemaker" + Fore.RESET + " wins - No Turns Left")
      if(codemaker == 1):
        user1Points = user1Points + 1
      else:
        user2Points = user2Points + 1
    else:
      DrawTable(B, H)
      print("_________________")
      print("| " + Colours[Answer[0] - 1] + Fore.RESET + "| " + Colours[Answer[1] - 1] + Fore.RESET + "| " + Colours[Answer[2] - 1] + Fore.RESET + "| " + Colours[Answer[3] - 1] + Fore.RESET + "|")
      print("-----------------")
      print()
      print()
      print(Fore.YELLOW + "Codebreaker" + Fore.RESET + " wins - The correct answer was found")
    print()
    stop = input("Press Enter To Continue")
    if(codemaker == 1):
      codemaker = 2
    else:
      codemaker = 1
  print()
  print()
  print(Fore.CYAN + "FINAL SCORES : ")
  print(user1Name + "'s points > " + str(user1Points))
  print(user2Name + "'s points > " + str(user2Points))
  if(user1Points == user2Points):
    print("It's a " + Fore.YELLOW + "DRAW")
  elif(user1Points > user2Points):
    print(Fore.GREEN + user1Name + " WINS")
  else:
    print(Fore.GREEN + user2Name + " WINS")
  print()
  stop = input("Press Enter To Continue")
  



    
    
def Options():
  global numberAssist
  os.system('cls')
  print()
  print(" .d88888b.           888    d8b        ")
  print("d88P   Y88b          888    Y8P                            ")
  print("888     888          888                                   ")
  print("888     888 88888b.  888888 888  .d88b.  88888b.  .d8888b  ")
  print("888     888 888  88b 888    888 d88  88b 888  88b 88K      ")
  print("888     888 888  888 888    888 888  888 888  888  Y8888b. ")
  print("Y88b. .d88P 888 d88P Y88b.  888 Y88..88P 888  888      X88 ")
  print("  Y88888P   88888P     Y888 888   Y88P   888  888  88888P' ")
  print("            888                                            ")
  print("            888                                            ")
  print("            888                                           ")
  print()
  print(Fore.CYAN + "OPTIONS :")
  print("1 > Activate Number Assist")
  print("2 > Deactivate Number Assist")
  print()
  choice = input("Enter your choice (or nothing to return to menu) > ")
  if(choice == "1"):
    numberAssist = True
    stop = input("Number Assist Activated")
    print()
    print()
    print()
    print()
    Options()
  elif(choice == "2"):
    numberAssist = False
    stop = input("Number Assist Deactivated")
    print()
    print()
    print()
    print()
    Options()
  else:
    print()
    print()
    print()
    print()




def Instructions():
  os.system('cls')
  print()
  print("8888888                   888                              888    d8b                            ")
  print("  888                     888                              888    Y8P                            ")
  print("  888                     888                              888                                   ")
  print("  888   88888b.  .d8888b  888888 888d888 888  888  .d8888b 888888 888  .d88b.  88888b.  .d8888b  ")
  print("  888   888  88b 88K      888    888P    888  888 d88P     888    888 d88  88b 888  88b 88K      ")
  print("  888   888  888  Y8888b. 888    888     888  888 888      888    888 888  888 888  888  Y8888b. ")
  print("  888   888  888      X88 Y88b.  888     Y88b 888 Y88b.    Y88b.  888 Y88..88P 888  888      X88 ")
  print("8888888 888  888  88888P'   Y888 888       Y88888   Y8888P   Y888 888   Y88P   888  888  88888P'")
  print()
  print("Welcome to Mastermind in Python!")
  print("This is an unofficial version developed by " + Fore.YELLOW + "Thomas McCarthy" + Fore.RESET + ", lead (and sole) programmer of " + Fore.BLUE + "Chillaxe Games")
  print()
  print("Mastermind is a board game designed for 2 players. At the start of each round, one player is assigned as the " + Fore.YELLOW + "Codemaker" + Fore.RESET + ", and the other as the " + Fore.YELLOW + "Codebreaker")
  print()
  print("The Mastermind board is made up of 12 rows of 4 holes, as depicted below:\n")
  E = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
  H = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
  DrawTable(E, H)
  print()
  print("At the start of the game, the " + Fore.YELLOW + "Codemaker" + Fore.RESET + " creates a sequence of 4 coloured pegs from the available 6 colours:")
  print(Fore.RED + "⬤ " + Fore.GREEN + " ⬤")
  print(Fore.BLUE + "⬤ " + Fore.CYAN + " ⬤")
  print(Fore.MAGENTA + "⬤ " + Fore.YELLOW + " ⬤")
  print()
  print("This sequence is the hidden code that the " + Fore.YELLOW + "Codebreaker" + Fore.RESET + " must discover.")
  print("To do this, they must create their own sequences from the same 6 colours, in the hope of matching the hidden code created by the " + Fore.YELLOW + "Codemaker" + Fore.RESET + ". As the number of rows suggests, the " + Fore.YELLOW + "Codebreaker" + Fore.RESET + " has 12 attempts to get the right answer.")
  print()
  print("To help the " + Fore.YELLOW + "Codebreaker" + Fore.RESET + " complete this task, the " + Fore.YELLOW + "Codemaker" + Fore.RESET + " must place between 0 and 4 " + Fore.WHITE + " white " + Fore.RESET + "and" + Fore.BLACK + " black " + Fore.RESET + "key pegs after each guess.")
  print("A black peg (" + Fore.BLACK + "🞉" + Fore.RESET + ") indicates that a correctly coloured peg has been placed in the correct space.")
  print("A white peg (" + Fore.WHITE + "🞉" + Fore.RESET + ") indicates that a correctly coloured peg has been placed in the wrong space.")
  print("No peg indicates an incorrectly coloured peg has been used.")
  print("There is " + Fore.RED + "no correlation" + Fore.RESET + " between the order of the key pegs and the order of the code pegs")
  print()
  print("The round ends when either the " + Fore.YELLOW + "Codebreaker" + Fore.RESET + " has broken the code, or is out of moves.")
  print("After all rounds have been played, the game ends. In normal Mastermind, the winner is determined by how many points each player scored (based on the number of turns it takes for their codes to be broken). However, due to the nature of the computer, the Single Player match winner is determined based on the number of round wins that have been earned.")
  print()
  stop = input("Press Enter to Return > ")





game = 0
numberAssist = False
while(game == 0):
  os.system('cls')
  print()
  print("888b     d888        d8888  .d8888b. 88888888888 8888888888 8888888b.  888b     d888 8888888 888b    888 8888888b.")
  print("8888b   d8888       d88888 d88P  Y88b    888     888        888   Y88b 8888b   d8888   888   8888b   888 888   Y88b")
  print("88888b.d88888      d88P888 Y88b.         888     888        888    888 88888b.d88888   888   88888b  888 888    888")
  print("888Y88888P888     d88P 888  Y888b.       888     8888888    888   d88P 888Y88888P888   888   888Y88b 888 888    888")
  print("888 Y888P 888    d88P  888     Y88b.     888     888        8888888P   888 Y888P 888   888   888 Y88b888 888    888")
  print("888  Y8P  888   d88P   888        888    888     888        888 T88b   888  Y8P  888   888   888  Y88888 888    888")
  print("888       888  d8888888888 Y88b  d88P    888     888        888  T88b  888       888   888   888   Y8888 888  .d88P")
  print("888       888 d88P     888   Y8888P      888     8888888888 888   T88b 888       888 8888888 888    Y888 8888888P")
  print("                                   _ __ _   ___  _ _ ___ _  _ ____ __ _")
  print("                                   | | \|   |--'  Y   |  |--| [__] | \|")
  print()
  time.sleep(0.25)
  print("Welcome to " + Fore.BLUE + "Mastermind in Python")
  print("'Mastermind' designed by " + Fore.YELLOW + "Mordecai Meirowitz")
  print("Developed by " + Fore.YELLOW + "Thomas McCarthy")
  print("This is an unofficial version, made for the sheer " + Fore.RED + "hell" + Fore.RESET + " of it. No copyright infringement is intended.")
  print()
  time.sleep(0.25)
  valid = 0
  while(valid == 0):
    print()
    print("--------------------------------------------------")
    print()
    print(Fore.CYAN + "MENU :")
    print("1 > Single Player (vs Computer)")
    print("2 > Two Player")
    print("3 > Instructions")
    print("4 > Options")
    print("5 > " + Fore.RED + "Quit")
    mode = input("Choice > ")
    print()
    print("--------------------------------------------------")
    print()
    if(mode == "1"):
      valid = 1
      SinglePlayer()
    elif(mode == "2"):
      valid = 1
      TwoPlayer()
    elif(mode == "3"):
      valid = 1
      Instructions()
    elif(mode == "4"):
      valid = 1
      Options()
    elif(mode == "5"):
      valid = 1
      game = 1
      exit = input("Press enter to quit > Thanks for playing! ")
    else:
      print("Invalid Entry > Try again!")

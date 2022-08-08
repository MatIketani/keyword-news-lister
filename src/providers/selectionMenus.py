from providers import data
from providers import news

option = None

# #
# MENUS
# #

def mainMenu():
  global option
  while(True):
    print("WELCOME TO G1 KEYWORD ENGINE")
    print("[1] Start")
    print("[2] Exit")

    option = int(input("> "))

    if option == 1:
      genreSelection()
    elif option == 2:
      break
    else:
      print("INVALID OPTION")

def genreSelection():
  print("GENRE SELECTION")

  for k, v in zip(range(len(data.genres)), data.genres.keys()):
    print("[" + str(k+1) + "] " + v)

  option = int(input("> "))

  if (option in range(2, 5)):
    keywordSelection(option, False)
  elif(option == 1):
    stateSelection()
  else:
    print("INVALID OPTION")

def stateSelection():
  print("SELECT THE STATE")
  
  for k, v in zip(range(len(data.brStates)), data.brStates.keys()):
    print("[" + str(k+1) + "] " + v)

  option = int(input("> "))

  if(option in range(1, len(data.brStates)+1)):
    keywordSelection(option, True)
  else:
    print("INVALID OPTION")
  

def keywordSelection(menu: int, isState: bool):
  print("TYPE YOUR KEYWORDS (use 'stop' to stop listening): ")

  keywords = []
  count = 0

  while(count <= 10):
    count = count + 1
    keyword = input("> ")
    keywords.append(keyword)

  keywords.pop()

  if(isState):
    news.listNews(menu, keywords, True)
  else:
    news.listNews(menu, keywords, False)

mainMenu()
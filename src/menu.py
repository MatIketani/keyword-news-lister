# #
# DATA
# #

brStates = {
  "AC": "http://pox.globo.com/rss/g1/ac/",
  "AL": "http://pox.globo.com/rss/g1/al/",
  "AP": "http://pox.globo.com/rss/g1/ap/",
  "AM": "http://pox.globo.com/rss/g1/am/",
  "BA": "http://pox.globo.com/rss/g1/ba/",
  "CE": "http://pox.globo.com/rss/g1/ce/",
  "DF": "http://pox.globo.com/rss/g1/df/",
  "ES": "http://pox.globo.com/rss/g1/es/",
  "GO": "http://pox.globo.com/rss/g1/go/",
  "MA": "http://pox.globo.com/rss/g1/ma/",
  "MT": "http://pox.globo.com/rss/g1/mt/",
  "MS": "http://pox.globo.com/rss/g1/ms/",
  "MG": "http://pox.globo.com/rss/g1/mg/",
  "PA": "http://pox.globo.com/rss/g1/pa/",
  "PB": "http://pox.globo.com/rss/g1/pb/",
  "PR": "http://pox.globo.com/rss/g1/pr/",
  "PE": "http://pox.globo.com/rss/g1/pe/",
  "PI": "http://pox.globo.com/rss/g1/pi/",
  "RJ": "http://pox.globo.com/rss/g1/rj/",
  "RN": "http://pox.globo.com/rss/g1/rn/",
  "RS": "http://pox.globo.com/rss/g1/rs/",
  "RO": "http://pox.globo.com/rss/g1/ro/",
  "RR": "http://pox.globo.com/rss/g1/rr/",
  "SC": "http://pox.globo.com/rss/g1/sc/",
  "SP": "http://pox.globo.com/rss/g1/sp/",
  "SE": "http://pox.globo.com/rss/g1/se/",
  "TO": "http://pox.globo.com/rss/g1/to/",
}

genres = {
  "States": brStates,
  "Brazil": "http://pox.globo.com/rss/g1/brasil/",
  "Tech": "http://pox.globo.com/rss/g1/tecnologia/",
  "Economy": "http://pox.globo.com/rss/g1/economia/",
  "Politics": "http://pox.globo.com/rss/g1/politica/"
}

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

  for k, v in zip(range(len(genres)), genres.keys()):
    print("[" + str(k+1) + "] " + v)

  option = int(input("> "))

  if (option in range(2, 5)):
    keywordSelection(option)
  elif(option == 1):
    stateSelection()
  else:
    print("INVALID OPTION")

def stateSelection():
  print("SELECT THE STATE")
  
  for k, v in zip(range(len(brStates)), brStates.keys()):
    print("[" + str(k+1) + "] " + v)

  option = int(input("> "))

  if(option in range(1, len(brStates)+1)):
    keywordSelection(option, True)
  else:
    print("INVALID OPTION")
  

def keywordSelection(menu: int, isState: bool):
  print("MENU KEYWORD")

mainMenu()
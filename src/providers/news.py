from providers import data
from providers import words
import requests
from bs4 import BeautifulSoup as bs

##  NEWS FILTER

def listNews(genre: int, keywords: list, isState: bool):
  if(isState):
    page = bs(requests.get(data.brStates[list(data.brStates)[genre-1]]).content, "xml")
  else:
    page = bs(requests.get(data.genres[list(data.genres)[genre-1]]).content, "xml")

  all_news = page.find_all("item")

  for n in all_news:
    link = n.find("link").text
    description = n.find("description").text

    matchingPercentage = words.compareKeywordsAndText(keywords, description)

    if(matchingPercentage > 0.6):
      print("[REQUEST FOUND] " + link)
    else:
      pass
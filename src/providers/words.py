import spacy

from string import punctuation

# #
#
# Spacy configuration
# 
# #

language = spacy.load("pt_core_news_sm")

# #
#
# Get keywords from a specific text
# 
# #

def getKeywords(content: str) -> list:
  result = []
  word_classes = ["PROPN", "ADJ", "NOUN"]
  doc = language(content.lower())

  for token in doc:
    if(token.text in language.Defaults.stop_words or token.text in punctuation):
      continue

    if(token.pos_ in word_classes):
      result.append(token.text)

    return list(set(result))


# #
#
# Compare keywords lists
#
# #

def compareLists(x: list, y: list) -> float:
  return len(set(x) & set(y)) / float(len(set(x) | set(y))) * 100
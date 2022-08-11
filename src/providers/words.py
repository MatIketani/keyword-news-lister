# #
#
# Compare keywords lists
#
# #

def compareKeywordsAndText(keywords: list, content: list):
  count = 1

  content = content.lower().split(" ")

  for w in content:
    if(w in keywords):
      count = count + 1

  return count / len(keywords)
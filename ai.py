import openai
import random
from english_words import get_english_words_set
openai.api_key = ""
#a = openai.Model.list()
#print(a)
#print(openai.Model.retrieve("text-davinci-003"))

def insult(friend, feature):
  web2set = list(get_english_words_set(['web2']))
  n = len(web2set)
  #Insults = {"Aaryaman" : [" he looks stupid"], 
  #           "Maanav" : ["he shat the bed with Sung", "he has a gigantic belly", "P-dawg rejected him", 
  #                       "what happened in that cs class", "how Aadtiya whips him on a daily basis"]}
  if feature != "":
    return openai.Completion.create(
      model="text-davinci-003",
      prompt="Insult my friend " + friend + " about " + feature + "",
      max_tokens=50,
      temperature=0
    )["choices"][0]["text"]
  else:
    r = random.randint(0, n-1)
    r2 = random.randint(0, n-1)
    feature = web2set[r]
    f2 = web2set[r2]
    return openai.Completion.create(
      model="text-davinci-003",
      prompt="Insult my friend " + friend + " by using his liking for " + feature + " and connect it to " + f2,
      max_tokens=50,
      temperature=0
    )["choices"][0]["text"]

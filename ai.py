import openai
import random
openai.api_key = ""
#a = openai.Model.list()
#print(a)
#print(openai.Model.retrieve("text-davinci-003"))
arr = ["beard", "face"]

def insult(friend, feature):
  Insults = {"Aaryaman" : [" he looks stupid"], 
             "Maanav" : ["he shat the bed with Sung", "he has a gigantic belly", "P-dawg rejected him", 
                         "what happened in that cs class", "how Aadtiya whips him on a daily basis"]}
  if feature != "":
    return openai.Completion.create(
      model="text-davinci-003",
      prompt="Insult my friend" + friend + "by" + feature + "",
      max_tokens=50,
      temperature=0
    )["choices"][0]["text"]
  else:
    r = random.randint(0, 100000)
    feature = Insults[friend][random.randint(0, len(Insults[friend])-1)]
    return openai.Completion.create(
      model="text-davinci-003",
      prompt="Insult my friend" + friend + "by saying something about how" + feature,
      max_tokens=50,
      temperature=0
    )["choices"][0]["text"]

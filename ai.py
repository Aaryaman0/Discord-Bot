import openai
openai.api_key = ""
#a = openai.Model.list()
#print(a)
#print(openai.Model.retrieve("text-davinci-003"))
arr = ["beard", "face"]

def insult(friend, feature):
  return openai.Completion.create(
    model="text-davinci-003",
    prompt="Insult my friend" + friend + "by saying something about how his" + feature + "is weird or stupid",
    max_tokens=50,
    temperature=0
  )["choices"][0]["text"]

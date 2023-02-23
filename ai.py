import openai
openai.api_key = ""
#a = openai.Model.list()
#print(a)
#print(openai.Model.retrieve("text-davinci-003"))
print(openai.Completion.create(
  model="text-davinci-003",
  prompt="Insult my friend Hans by saying something about how his beard is weird",
  max_tokens=50,
  temperature=0
)["choices"][0]["text"])
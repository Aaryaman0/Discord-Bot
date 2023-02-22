import openai
openai.api_key = ""
#a = openai.Model.list()
#print(a)
print(openai.Model.retrieve("text-davinci-003"))

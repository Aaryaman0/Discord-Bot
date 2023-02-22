import openai
openai.api_key = "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"
#a = openai.Model.list()
#print(a)
print(openai.Model.retrieve("text-davinci-003"))
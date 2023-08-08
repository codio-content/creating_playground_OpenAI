#CODIO SOLUTION BEGIN
import os
import openai
import secret
openai.api_key=secret.api_key

# open the file and read its content
with open('playground.txt', 'r') as file:
    file_content = file.read()

# if the code word for clearing the content is present we clear the contents
if '//clear//' in file_content:
    with open("playground.txt", "w") as file:
        file.close()
elif '//joke//' in file_content:
    # generate a joke using GPT-3
    joke_prompt = "Tell me a good joke."
    joke_response = openai.Completion.create(model="text-davinci-002", 
                                             prompt=joke_prompt,
                                             max_tokens=256)
    joke = joke_response['choices'][0]['text'].strip()

    # append the joke to the file
    with open("playground.txt", "a") as file:
        file.write("\n")
        file.write(joke)
else:
    # default behaviour
    prompts = file_content
    response = openai.Completion.create(model="text-davinci-002", 
                                        prompt=prompts,
                                        max_tokens=256,
                                        top_p=0.1)
    txt_response=response['choices'][0]['text'].strip()

    #open our file, and append to it
    with open("playground.txt", "a") as file:
        file.write(("\n"))
        file.write((txt_response))
# CODIO SOLUTION END
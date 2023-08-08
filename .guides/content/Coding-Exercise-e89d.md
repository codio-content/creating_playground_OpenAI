For our coding exercise we are going to create an extra feature similar to `//clear//`. 

You can implement a feature where certain keywords trigger GPT-3 to generate specific types of content. For example,` //joke//` could make the program generate a random joke, `//quote//` could trigger a famous quote generation, and `//news//` could lead to a summary of the day's top news.

For our assignment modify the code for your program so that if the user types in `//joke//` a joke will be outputted. Have your code so that `//clear//` has a priority than joke. Meaning if both keywords are present it will just clear the page. 

**Be sure** to click the Try It to run your box.
{Try it!}(python3 playground.py 18)

{Check It!|assessment}(code-output-compare-3599793239)


|||guidance
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
                                             max_tokens=256,
                                             top_p=0.5)
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
|||
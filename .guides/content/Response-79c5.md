On the top left we have our Python file. On the bottom left we have the empty text file where the user will be able to simply write their prompts and generate and get their responses from. 

For starters, we are going to use the same structure we have been using before to generate our responses. First, let's get our libraries.
```python
import os
import openai
import secret
openai.api_key=secret.api_key
```


We need to read our file and just put the contents of it as our prompt.  
``` python
#open the file
file = open("playground.txt", "r")
#read each line
filelines = file.readlines()
#put all the lines in a single variable
all_lines = ""
for line in filelines:
    all_lines += line
#close the file
file.close()
``` 
{Try it!}(python3 playground.py 3)
It is customary to close the file when done with it. To test our code, we will try a couple of things. 
On the top left in our Python file try running the following code.
```python 
print("hello world")
```
{Try it!}(python3 playground.py 4)

Now instead of printing `hello world` we are going to print the `all_lines`, to try and see the content of the `playground.txt` file. 
```python
print(all_lines)
```
{Try it!}(python3 playground.py 5)

Since our playground has no content in it yet we are going to get a blank response. We should have the Codio IDE message that our code successfully ran. 

Now let's try adding the following text on our `.txt` file (bottom left), and try running our file again since now our playground will not be empty.
```
write a tagline for an ice cream shop.
```
{Try it!}(python3 playground.py 6)

It should print out `write a tagline for an ice cream shop.`. Now that we know we have access to the contents of our file let's assign it as the prompt instead of printing it. 
```python
prompts = all_lines
```
{Try it!}(python3 playground.py 7)

We typically employ the following code to prompt users and capture the AI response:

```
response = openai.Completion.create(model="text-davinci-002", 
                                      prompt=prompts,
                                      max_tokens=256,
                                      top_p=0.1)
txt_response=response['choices'][0]['text'].strip()
print(txt_response)
```
{Try it!}(python3 playground.py 8)


Now that we can get it to generate a response on the content of our text file we are going to have it write down the response in that same text file. For that we need to first open our file then simply add the response in to the text file instead of printing it. 
```python
#open our file, and append to it
f = open("playground.txt", "a")
#write the response we want to append 
f.write((txt_response))
#close our file
f.close()
```
{Try it!}(python3 playground.py 9)

From that we realize it generates our response on the same line. Delete the text in the playground file. Have it go back to simply:
```
Write a tagline for an ice cream shop
```
Before we write our response we are going to make sure it adds to a new line so we will change our code to the following:
```python
#write the response we want to append  
f.write(("\n"))
f.write((txt_response))
```
{Try it!}(python3 playground.py 10)

Feel free to try it with different prompts. For example:
```
Give me 5 movie recommendations.
```
{Try it!}(python3 playground.py 11)

Let's just say it's a pain to keep erasing. Let's add some code that will clear our text file for us. We will use the key word `//clear//` in our playground to know to clear it instead of generating anything. In other words, if in a our file we see the `//clear//` keyword our program instead of generating anything will give us a blank page. Copy and paste the following in our code above the code we have already written. For the `else` case, we are going to make the code we have already written the contents for it.

```python
# if the code word is present we clear the contents
if '//clear//' in open('playground.txt').read():
  open("playground.txt", "w").close()
else:
```
Opening a file in "write" mode clears it. Again we have to close it after we are done with it. Inside the else statement we can indent the rest of the code we have previously written 

{Try it!}(python3 playground.py 12)

{Check It!|assessment}(multiple-choice-2774471357)

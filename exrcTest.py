import os

# Test 1: joke_keyword
# write the keyword to the file
with open('playground.txt', 'w') as file:
    file.write('//joke//')

# run the program
os.system('python playground.py')

# check if the file is not empty (a joke should have been written to it)
with open('playground.txt', 'r') as file:
    if file.read() == '':
        print("Test 1 failed: The file is empty.")
    else:
        print("Test 1 passed: A joke has been written to the file.")

# Test 2: clear_keyword
# write some content to the file
with open('playground.txt', 'w') as file:
    file.write('//joke//')

# write the keyword to the file
with open('playground.txt', 'w') as file:
    file.write('//clear//')

# run the program
os.system('python playground.py')

# check if the file is empty (it should have been cleared)
with open('playground.txt', 'r') as file:
    if file.read() != '':
        print("Test 2 failed: The file is not empty.")
    else:
        print("Test 2 passed: The file has been cleared.")

print("Nice Job, it works!")

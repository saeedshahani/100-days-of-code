#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

with open("./Day 24/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)
with open("./Day 24/Input/Letters/starting_letter.txt", "r") as starting_letter:
    content = starting_letter.read()
    for name in names:
        name = name.strip("\n")
        new_content = content.replace(PLACEHOLDER,name)
        with open(f"./Day 24/Output/ReadyToSend/{name}.txt", "a") as save_letter:
            save_letter.writelines(new_content)
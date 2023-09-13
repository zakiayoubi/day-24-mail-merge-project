letter = open("../Mail Merge Project Start/Input/Letters/starting_letter.txt", mode='r')
letter_content = letter.read()


names = open("../Mail Merge Project Start/Input/Names/invited_names.txt", mode='r')
list_of_names = names.readlines()


for name in list_of_names:
    modified_content = letter_content.replace("[name]", name.strip())
    completed_letter = open(f"../Mail Merge Project Start/Output/ReadyToSend/letter_for_{name.strip()}.txt", mode="w")
    completed_letter.write(modified_content)
    completed_letter.close()

names.close()
letter.close()








# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
#
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#     Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#         Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
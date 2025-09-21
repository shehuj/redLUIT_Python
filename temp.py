def find_acronym(acronym):
    with open("acronyms.txt", "r") as file:
        for line in file:
            if line.startswith(acronym + ' -'):
                return line.strip().split(' - ')[1]
    return None
# Ask the user what acronym they want to check
# look_up = input("Enter acronym to look up: ").upper()
acronym = input("What acronym do you want to add?: \n")
# Then ask the user for the definition
definition = input("What is the definition: \n")
## Open the file in append mode, to add the new acronym and definition at the end of the file.
with open("acronyms.txt", "a") as file:
    file.write(acronym + '-' + definition + '\n')
## Open the file in read mode to check if the acronym already exists
# with open("acronyms.txt", "r") as file:
## Open the file in write mode, an existing file will be erased and overrriten to add the new acronym and definition
# with open("acronyms.txt", "w") as file:
## Convert the acronym to uppercase
#    look_up = acronym.upper()
# Write the acronym and definition to the file

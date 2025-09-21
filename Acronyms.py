def find_acronym():
    look_up = input("What software acronym would you like to look up: \n")

    found = False
    try:
        with open("acronyms.txt", "r") as file:
            for line in file:
                if look_up in line:
                    print(line)
                    found = True
                    break
    except FileNotFoundError as e:
        print("File not found.")
        # to stop the function if the file is not found
        return

    if not found:
        print("Acronym does not exist.")

def add_acronym():
    acronym = input("What acronym do you want to add?: \n")
    definition = input("What is the definition: \n")
    with open("acronyms.txt", "a") as file:
        file.write(acronym + ' - ' + definition + '\n')

def main():
    # Ask the user if they want to look up an acronym or add a new one
        choice = input("Would you like to find an acronym (F), add a new acronym (A), or quit (Q)? \n").upper()
        if choice == 'F':
            find_acronym()
        elif choice == 'A':
            add_acronym()
        elif choice == 'Q':
            print("Exiting the program.")
        else:
            print("Invalid option. Please choose L, A, or Q.")

main()
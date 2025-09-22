import random
import string

# define the number of instance names to generate
num_instace_names = int(input("Enter number of instances to generate names for: \n"))
print("++++++++++++++++++++++++++++++++++++ \n")

# define the departments
departments = ['Accounting', 'FinOps', 'Marketing']

rand_letter = ''
rand_num = ''
random = random.Random()


# generate instance names, and set limit to not more than 5 at a time
if num_instace_names > 5:
    print("You can only generate up to 5 instance names at a time. Please try again with a lesser number.")
    num_instace_names = 6
else:
    print(f"Generating {num_instace_names} instance names. \n")
    print("++++++++++++++++++++++++++++++++++++ \n")

for i in range(num_instace_names):
    dept = input("For what department is this instance: \n")
    rand_num = random.randint(10001, 99999)
    rand_letter = ''.join(random.choices(string.ascii_lowercase, k=4))

# Output the instance name
    instance_name = f"redLUIT-{dept}{rand_num}{rand_letter}"
    print(instance_name)

# Check if the department is valid
    if dept not in departments:
        print("Invalid department. Please choose from the following:")
        for dept in departments:
            print(dept)
        break
    else:
        print(f"Instance name {instance_name} has been created for the {dept} department.")
        print("========================================= \n")
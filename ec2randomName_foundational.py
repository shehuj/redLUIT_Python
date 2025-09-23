import random
import string

# define the number of instance names to generate
number_of_instances = int(input("Enter number of instances to generate names for: \n"))
print("number_of_instances: ", number_of_instances)
print("++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++ \n")

# define the departments
department_names = ('Accounting', 'FinOps', 'Marketing', 'IT')
names = input("For what department is this instance: \n").upper()
# set an case sensitive input for department names
if names not in department_names:
    print("Invalid department. Please choose from the following:")
    for dept in department_names:
        print(dept)
    exit()
else:
    print("Valid department.")
print("Department: ", names)


# Generate instance names
rand_num = random.randint(1000, 9999)
rand_letter = ''.join(random.choices(string.ascii_lowercase, k=4))
instance_name = f"redLUIT-{names}{rand_num}{rand_letter}"

# Generate instance names with some limitations to amount of names to be generated.
for i in range(number_of_instances):
    rand_num = random.randint(1000, 9999)
    rand_letter = ''.join(random.choices(string.ascii_lowercase, k=4))
    instance_name = f"redLUIT-{names}{rand_num}{rand_letter}"
    print("Instance name: ", instance_name)
    if number_of_instances > 5:
        print("You can only generate up to 5 instance names at a time. Please try again with a lesser number.")
        break
    else:
        print(f"Generating {number_of_instances} instance names. \n")
        print("++++++++++++++++++++++++++++++++++++ \n")
        print(f"Instance name {instance_name} has been created for the {names} department .")
print("==================================================")

import random
import string

# define the number of instance names to generate
number_of_instances = int(input("Enter number of instances to generate names for: \n"))
print("number_of_instances: ", number_of_instances)
print("++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++ \n")

# define the departments
department_names = ('Accounting', 'FinOps', 'Marketing', 'IT')
names = input("For what department is this instance: \n")
print("Department: ", names)


# generate instance names, and set limit to not more than 5 at a time
rand_num = random.randint(1000, 9999)
rand_letter = ''.join(random.choices(string.ascii_lowercase, k=4))
instance_name = f"redLUIT-{names}{rand_num}{rand_letter}"

# Loop to generate instance names
for i in range(number_of_instances):
    rand_num = random.randint(1000, 9999)
    rand_letter = ''.join(random.choices(string.ascii_lowercase, k=4))
    instance_name = f"redLUIT-{names}{rand_num}{rand_letter}"
    print("Instance name: ", instance_name)
    if number_of_instances > 5:
        print("You can only generate up to 5 instance names at a time. Please try again with a lesser number.")
        break
print("==================================================")
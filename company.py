from employee import Employee, SalaryEmployee, HourlyEmployee, CommissionEmployee

class Company:
    def __init__(self):
        self.employees = []
    
    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def display_employees(self):
        print("Current employees in the company: \n")
        for emp in self.employees:
            print(emp.fname, emp.lname)


    def pay_employees(self):
        print("Paying employees...")
        for emp in self.employees:
            print("Paycheck for:", emp.fname, emp.lname)
            print(f'Amount: ${emp.calculate_paycheck():,.2f}')
            print("------------------------")
            # Here you could integrate with a payment system or API

def main():
    my_company = Company()
    
    employee1 = SalaryEmployee("Sarah", "Hess", 50000)
    employee2 = HourlyEmployee("Lee", "Smith", 25, 50)
    employee3 = CommissionEmployee("Bob", "Brown", 30000, 5, 200)
#    employee4 = SalaryEmployee("Jane", "Smith", 60000)
    
    my_company.add_employee(employee1)
    my_company.add_employee(employee2)
    my_company.add_employee(employee3)
 #   my_company.add_employee(employee4)

    print("Company Employees and their Weekly Paychecks:")
    
    my_company.display_employees()
    my_company.pay_employees()

main()
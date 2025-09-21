class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def calculate_paycheck(self):
        return self.hourly_rate * self.hours_worked

class SalaryEmployee(Employee):
    def __init__(self, fname, lname, salary):
        super().__init__(fname, lname)
        self.salary = salary
    
    def calculate_paycheck(self):
        return self.salary/52 # Assuming salary is annual, divide by 52 weeks 
        
class HourlyEmployee(Employee):
    def __init__(self, fname, lname, weekly_hours, hourly_rate):
        super().__init__(fname, lname)
        self.weekly_hours = weekly_hours
        self.hourly_rate = hourly_rate

    def calculate_paycheck(self):
        return self.weekly_hours*self.hourly_rate
    
class CommissionEmployee(SalaryEmployee):
    def __init__(self, fname, lname, sales_num, com_rate, salary):
        super().__init__(fname, lname, salary)
        self.sales_num = sales_num
        self.com_rate = com_rate
    
    def calculate_paycheck(self):
        regular_salary = super().calculate_paycheck()
        total_commission = self.sales_num*self.com_rate
        return regular_salary+total_commission
    
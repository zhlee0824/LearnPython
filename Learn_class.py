class Employee:
    increase_pay = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+"."+last+"@company.com"

    def fullname(self):
        return(self.first+" "+self.last)

    def raise_pay(self):
        self.pay *= self.increase_pay
    
    #def email(self):
    #    return self.first+"."+self.last+"@company.com"

    @classmethod
    def set_raise_amount(cls, amount):
        cls.increase_pay = amount

    @classmethod
    def from_string(cls, str):
        first, last, pay = str.split("-")
        return cls(first, last, pay)
    @staticmethod
    def is_workday(day):
        if(day.weekday() == 5)or(day.weekday() == 6):
            return False
        else:
            return True

    
class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees):
        super().__init__(first, last, pay)
        self.employees = employees
    
    def append_employee(self, emp):
        if(emp not in self.employees):
            self.employees.append(emp)

    def remove_employee(self, emp):
        if(emp in self.employees):
            self.employees.remove(emp)
    

emp1 = Developer("Louis", "Lee", 60000, "Java")
emp2 = Developer("Corey", "Sch", 80000, "Python")

mang_1 = Manager("Knight", "Kavis", 90000, [])

mang_1.append_employee(emp1)
mang_1.append_employee(emp2)

for emp in mang_1.employees:
    print(emp.email)
#print(emp1.fullname())
#print(emp2.pay)
#Employee.set_raise_amount(1.06)

#print(Employee.increase_pay)
#print(emp2.increase_pay)
#print(emp1.increase_pay)

#print("Emp2 pay:", emp2.pay)

#emp3 = Employee.from_string("Jason-Doe-50000")

#print(emp3.email)

#import datetime
#day = datetime.date(2020, 11, 6) 
#print(Employee.is_workday(day))


#print(help(Developer))

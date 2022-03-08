class Employee:

    # Class variables
    empCount = 0

    # Data: Instance variables/initialize them in the constructor
    def __init__(self, empname, empcompany, empsalary):
        self.name = empname
        self.company = empcompany
        self.salary = empsalary
        self.tax = 0
        Employee.empCount += 1

    # Functions
    def printinfo(self):
        print(self.name.upper())
        print("-"*30)
        print("COMPANY     : ", self.company)
        print("SALARY      : ", self.salary)
        print("TAX         : ", self.tax)
        print("-"*30)
        print("\n")
 
    def setsalary(self, newsalary): # 16000 INR
        self.salary = newsalary
        self.calctax()

    def getsalary(self):
        return self.salary

    def calctax(self, pct=0.1): # pct = 0.1
        self.tax = pct * float(self.salary.split()[0])
        self.salary = str(float(self.salary.split()[0]) - self.tax) + ' INR'
        
    def calchike(self):
        pass


class newemployee(Employee):
    pass


class extEmployee(Employee):

    def __init__(self, empname, empcompany, empsalary, empdob):
        self.dob = empdob
        self.age = 0
        super().__init__(empname, empcompany, empsalary)

    def calcage(self):
        pass

    def printinfo(self):
        #super().printinfo()
        print(self.name.upper())
        print("AGE         : ", self.age)
        print("-"*30)
        print("COMPANY     : ", self.company)
        print("SALARY      : ", self.salary)
        print("TAX         : ", self.tax)
        print("-"*30)
        print("\n")    

# ------------------------------------------------------------------

e1 = newemployee('Anil', 'Infosys', '1600000 INR')
e1.calctax()
e1.printinfo()

# ------------------------------------------------------------------

e2 = extEmployee('Anil', 'Infosys', '1600000 INR', "10/12/1988")
e2.calctax()
e2.printinfo()

# ------------------------------------------------------------------


print("Polymorphic effects")
e = e2
e.printinfo()

# -------------------------------------------------------------------

# [LAB] implements calcage()

'''
>>> from datetime import datetime
>>> datetime.now()
datetime.datetime(2022, 3, 8, 12, 40, 52, 983469)
>>> datetime.now().year
2022
>>>
'''

e.printinfo()  # this should show the age as well
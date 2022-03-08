# Core Developer

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

# --------------------------------------------------------------------


# Application Developer

e1 = Employee('Anil', 'Oracle', '1600000 INR')
e1.printinfo()
e1.calctax(0.3)
e1.printinfo()

ED = { 'e1': {'name': 'Anil', 'company': 'Oracle', 'salary': "1600000 INR"},
       'e2': {'name': 'Sunil', 'company': 'Oracle', 'salary': "1700000 INR"},
       'e3': {'name': 'Ram', 'company': 'Oracle', 'salary': "1800000 INR"},
       'e4': {'name': 'Raj', 'company': 'Oracle', 'salary': "1900000 INR"},
       'e5': {'name': 'Kiran', 'company': 'Oracle', 'salary': "2000000 INR"},
}

e = []
for emp in ED.keys():
    obj = Employee(ED[emp]['name'], ED[emp]['company'], ED[emp]['salary'])
    e.append(obj)

for emp in e:
    emp.calctax(0.2)

for emp in e:
    emp.printinfo()


# -------------------------------------------------------------------


# [LAB] 10 mins

for emp in e:
    emp.calchike("15%")

for emp in e:
    emp.printinfo()  # this should show me updated salary along with tax calculated
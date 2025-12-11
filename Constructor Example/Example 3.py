#Constructor with multiple parameter

class demo:
    def __init__(self,empName,empID,empSalary, empDesg):
        self.empName=empName
        self.empID=empID
        self.empSalary=empSalary
        self.empDesg=empDesg

    def empInfo(self):
        print("EmpName: ",self.empName)
        print("EmpId: ",self.empID)
        print("EmpSalary: ",self.empSalary)
        print("EmpDesignation: ",self.empDesg)

d=demo("Pranav",1,100000,"Lead Tester")
d1=demo("Nikita",2,200000,"Lead Teste2")
d.empInfo()
print("--")
d1.empInfo()
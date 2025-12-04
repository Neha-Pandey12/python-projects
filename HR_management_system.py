#HR Employee Management System (classes + Inheritance +Polymorphism)
from typing import Dict,Any,List,Optional
#defining a class called Employee

class Employee:
    def __init__(self,emp_id:int,name:str,role:str):
        self.details:Dict[str,Any]={
            "id":emp_id,
            "name":name,
            "role":role
        }
    def calculate_salary(self)->float:
        raise NotImplementedError
    def __repr__(self)->str:
        return f"{self.details['role']}({self.details['id']}:{self.details['name']})"
    
class FullTime(Employee):
    def __init__(self,emp_id:int,name:str,base_salary:float,benefits:float=0.0,performance_percent:float=0.0):
        super().__init__(emp_id,name,"FullTime")
        self.details.update({
            "base_salary":base_salary,
            "benefits":benefits,
            "performance_percent":performance_percent
        })
    
    def calculate_salary(self)->float:
        base=self.details["base_salary"]
        benefits=self.details["benefits"]
        performance=self.details["performance_percent"]
        #performance bonus is determinded on the basis of base salary which is performance bonus is percent of base
        perf_bonus=base*(performance/100.0)
        total_salary=base+benefits+perf_bonus
        return round(total_salary,2)
    
class PartTime(Employee):
    def __init__(self,emp_id:int,name:str,hourly_rate:float,hrs_worked:float):
        super().__init__(emp_id,name,"Partime")
        self.details.update({
            "hourly_rate":hourly_rate,
            "hrs_worked":hrs_worked

        })

    def calculate_salary(self)->float:
        r=self.details["hourly_rate"]
        h=self.details["hrs_worked"]
        regular=min(h,40)*r
        overtime=max(0.0,h-40)*r*1.5
        total_salary=regular+overtime
        return round(total_salary,2)
class Intern(Employee):
    def __init__(self,emp_id:int,name:str,pocket_money:float,project_completed:bool=False):
        super().__init__(emp_id,name,"Intern")
        self.details.update({
            "pocket_money":pocket_money,
            "project_completed":project_completed
        })

    def calculate_salary(self)->float:
        get_salary=self.details["pocket_money"]
        bonus=100.0 if self.details["project_completed"] else 0.0
        total_salary=get_salary+bonus
        return round(total_salary,2)

class HRSystem:
    def __init__(self):
        self.employees:List[Employee]=[]
    def add_employee(self,e:Employee)->None:
        self.employees.append(e)
    def list_employees(self)->None:
        for e in self.employees:
            print(f"{e}->Slary: ${e.calculate_salary()}")
    def total_payroll(self)->float:
        return round(sum(e.calculate_salary() for e in self.employees),2)

def display():
    hr=HRSystem()

    hr.add_employee(FullTime(1,"Neha Pandey",base_salary=50000.0,benefits=5000.0,performance_percent=10.0))
    hr.add_employee(PartTime(2,"Shashwat Pokharel",hourly_rate=12.0,hrs_worked=45.0))
    hr.add_employee(Intern(3,"Chandan Yadav",pocket_money=4000.0,project_completed=True))

    print("Employee list and Monthly salaries:")
    hr.list_employees()

    print("\nTotal payroll:",hr.total_payroll())
if __name__=="__main__":
    display()

    

    
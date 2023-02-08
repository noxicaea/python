Employees = {}
Teamleaders = {}
Managers = {}


class Employees_function_Mixin:
    def get_uid(self):
        print(self.uid)
    
    def get_name(self):
        print(self.name)
    
    def get_job(self):
        print(self.job)
    
    def get_grade(self):
        print(self.grade)
    
    def get_year(self):
        print(self.year)
    
    def salary(self):
        if self.job ==  "E":
            self.salarys = 3000 + 500 * self.grade + 500 * self.year
        elif self.job == "T":
            self.salarys = 4000 + 800 * self.grade + 100 * self.year
        elif self.job == "M":
            self.salarys = 5000 + 1000 * (self.grade + self.year)
        return self.salarys

class Employee(Employees_function_Mixin):
    Max_grade = 10
    def __init__(self,name,job,grade,year,uid):
        self.name = name
        self.job = job
        self.grade = grade
        self.year = year
        self.uid = uid

class Teamleader(Employees_function_Mixin):
    Max_grade = 6
    def __init__(self,name,job,grade,year,uid):
        self.name = name
        self.job = job
        self.grade = grade
        self.year = year
        self.uid = uid

class Manager(Employees_function_Mixin):
    Max_grade = 3
    def __init__(self,name,job,grade,year,uid):
        self.name = name
        self.job = job
        self.grade = grade
        self.year = year
        self.uid = uid

def main():
    uid_total = 10000
    while True:
        print("1.录入,2.查询,3.升级,4.降级,5.退出")
        get = input()
        if get == "1":
            name = input("请输入姓名：")
            job = input("职位：(E.普通员工；T.组长；M.经理)：")
            while job != "E" and job != "T" and job != "M":
                print("输入错误！请重新输入！")
                job = input("职位：(E.普通员工；T.组长；M.经理)：")
            grade = int(input("级别："))
            if job == "E":
                while grade > Employee.Max_grade:
                    print("该职位最高级别为10！请重新输入！")
                    grade = int(input("级别："))
            elif job == "T":
                while grade > Teamleader.Max_grade:
                    print("该职位最高级别为6！请重新输入！")
                    grade = int(input("级别："))
            elif job == "M":
                while grade > Manager.Max_grade:
                    print("该职位最高级别为3！请重新输入！")
                    grade = int(input("级别："))
            year = int(input("工龄："))
            if job == "E":
                Employees[uid_total] = Employee(name,job,grade,year,uid_total)
            elif job == "T":
                Teamleaders[uid_total] = Teamleader(name,job,grade,year,uid_total)
            elif job == "M":
                Managers[uid_total] = Manager(name,job,grade,year,uid_total)
            print(f"录入成功！姓名：{name},职位：{job},级别：{grade},工龄：{year},工号：{uid_total}")
            print(Managers)
            uid_total += 1

        elif get == "2":
            inquiry = input("1.按工号查询,2.按职位查询：")
            if inquiry == "1":
                uid = int(input("请输入工号："))
                if uid in Employees.keys():
                    print(f"姓名：{Employees[uid].name}")
                    print(f"职位：{Employees[uid].job}")
                    print(f"级别：{Employees[uid].grade}")
                    print(f"工龄：{Employees[uid].year}")
                    print(f"工资：{Employees[uid].salary()}")
                elif uid in Teamleaders.keys():
                    print(f"姓名：{Teamleaders[uid].name}")
                    print(f"职位：{Teamleaders[uid].job}")
                    print(f"级别：{Teamleaders[uid].grade}")
                    print(f"工龄：{Teamleaders[uid].year}")
                    print(f"工资：{Teamleaders[uid].salary()}")
                elif uid in Managers.keys():
                    print(f"姓名：{Managers[uid].name}")
                    print(f"职位：{Managers[uid].job}")
                    print(f"级别：{Managers[uid].grade}")
                    print(f"工龄：{Managers[uid].year}")
                    print(f"工资：{Managers[uid].salary()}")
                else:
                    print("工号不存在！")
            elif inquiry == "2":
                job = input("请输入职位：")
                if job == "E":
                    print(f"目前普通员工有：{len(Employees)}人")
                    for i in Employees:
                        print(f"姓名：{Employees[i].name},工号：{Employees[i].uid}")
                elif job == "T":
                    print(f"目前组长有：{len(Teamleaders)}人")
                    for i in Teamleaders:
                        print(f"姓名：{Teamleaders[i].name},工号：{Teamleaders[i].uid}")
                elif job == "M":
                    print(f"目前经理有：{len(Managers)}人")
                    for i in Managers:
                        print(f"姓名：{Managers[i].name},工号：{Managers[i].uid}")

        elif get =="3":
            uid = int(input("请输入工号："))
            if uid in Employees.keys():
                print(f"{Employees[uid].name},工号:{Employees[uid].uid},当前职位:{Employees[uid].job+str(Employees[uid].grade)},工龄:{Employees[uid].year},工资:{Employees[uid].salary()}")
                update = int(input("请输入需要增加的级数："))
                if Employees[uid].grade + update > Employee.Max_grade:
                    Teamleaders[uid] = Teamleader(Employees[uid].name,"T",1,Employees[uid].year,Employees[uid].uid)
                    Employees.pop(uid)
                    print(f"升级成功！升级后的职位为{Teamleaders[uid].job+str(Teamleaders[uid].grade)}，工资为:{Teamleaders[uid].salary()}")
                else:
                    Employees[uid].grade += update
                    print(f"升级成功！升级后的职位为{Employees[uid].job+str(Employees[uid].grade)}，工资为:{Employees[uid].salary()}")
            elif uid in Teamleaders.keys():
                print(f"{Teamleaders[uid].name},工号:{Teamleaders[uid].uid},当前职位:{Teamleaders[uid].job+str(Teamleaders[uid].grade)},工龄:{Teamleaders[uid].year},工资:{Teamleaders[uid].salary()}")
                update = int(input("请输入需要增加的级数："))
                if Teamleaders[uid].grade + update > Teamleader.Max_grade:
                    Managers[uid] = Manager(Teamleaders[uid].name,"M",1,Teamleaders[uid].year,Teamleaders[uid].uid)
                    Teamleaders.pop(uid)
                    print(f"升级成功！升级后的职位为{Managers[uid].job+str(Managers[uid].grade)}，工资为:{Managers[uid].salary()}")
                else:
                    Teamleaders[uid].grade += update
                    print(f"升级成功！升级后的职位为{Teamleaders[uid].job+str(Teamleaders[uid].grade)}，工资为:{Teamleaders[uid].salary()}")
            elif uid in Managers.keys():
                print(f"{Managers[uid].name},工号:{Managers[uid].uid},当前职位:{Managers[uid].job+str(Managers[uid].grade)},工龄:{Managers[uid].year},工资:{Managers[uid].salary()}")
                update = int(input("请输入需要增加的级数："))
                if Managers[uid].grade + update > Manager.Max_grade:
                    Managers[uid].grade = 3
                    print(f"升级成功！升级后的职位为{Managers[uid].job+str(Managers[uid].grade)}，工资为:{Managers[uid].salary()}")
                else:
                    Managers[uid].grade += update
                    print(f"升级成功！升级后的职位为{Managers[uid].job+str(Managers[uid].grade)}，工资为:{Managers[uid].salary()}")
            else:
                print("工号不存在！")
        
        elif get == "4":
            uid = int(input("请输入工号："))
            if uid in Employees.keys():
                print(f"{Employees[uid].name},工号:{Employees[uid].uid},当前职位:{Employees[uid].job+str(Employees[uid].grade)},工龄:{Employees[uid].year},工资:{Employees[uid].salary()}")
                minus = int(input("请输入需要降级的级数："))
                if Employees[uid].grade - minus < 1:
                    Employees[uid].grade = 1
                    print(f"降级成功！降级后的职位为{Employees[uid].job+str(Employees[uid].grade)}，工资为:{Employees[uid].salary()}")
                else:
                    Employees[uid].grade -= minus
                    print(f"降级成功！降级后的职位为{Employees[uid].job+str(Employees[uid].grade)}，工资为:{Employees[uid].salary()}")
            elif uid in Teamleaders.keys():
                print(f"{Teamleaders[uid].name},工号:{Teamleaders[uid].uid},当前职位:{Teamleaders[uid].job+str(Teamleaders[uid].grade)},工龄:{Teamleaders[uid].year},工资:{Teamleaders[uid].salary()}")
                minus = int(input("请输入需要降级的级数："))
                if Teamleaders[uid].grade - minus < 1:
                    Employees[uid] = Employee(Teamleaders[uid].name,"E",10,Teamleaders[uid].year,Teamleaders[uid].uid)
                    Teamleaders.pop(uid)
                    print(f"降级成功！降级后的职位为{Employees[uid].job+str(Employees[uid].grade)}，工资为:{Employees[uid].salary()}")
                else:
                    Teamleaders[uid].grade -= minus
                    print(f"降级成功！降级后的职位为{Teamleaders[uid].job+str(Teamleaders[uid].grade)}，工资为:{Teamleaders[uid].salary()}")
            elif uid in Managers.keys():
                print(f"{Managers[uid].name},工号:{Managers[uid].uid},当前职位:{Managers[uid].job+str(Managers[uid].grade)},工龄:{Managers[uid].year},工资:{Managers[uid].salary()}")
                if Managers[uid].grade - minus < 1:
                    Teamleaders[uid] = Teamleader(Managers[uid].name,"T",6,Managers[uid].year,Managers[uid].uid)
                    Managers.pop(uid)
                    print(f"降级成功！降级后的职位为{Teamleaders[uid].job+str(Teamleaders[uid].grade)}，工资为:{Teamleaders[uid].salary()}")
                else:
                    Managers[uid].grade -= minus
                    print(f"降级成功！降级后的职位为{Managers[uid].job+str(Managers[uid].grade)}，工资为:{Managers[uid].salary()}")
        elif get == "5":
            break
        
        else:
            print("输入错误！请重新输入！")

if __name__ == "__main__":
    main()
import requests

class Employee():
    
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def get_employee(url):
        response = requests.get(url)
        return response
    
    @staticmethod
    def add_employee(url,data):
        response = requests.post(url,data=data)
        return response
    
    @staticmethod
    def update_employee(url,data):
        response = requests.put(url,data=data)
        return response
    
    @staticmethod
    def delete_employee(url):
        response = requests.delete(url)
        return response

class Department():
    
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def get_department(url):
        response = requests.get(url)
        return response

    @staticmethod
    def add_department(url,data):
        response = requests.post(url,data=data)
        return response

    @staticmethod
    def update_department(url,data):
        response = requests.put(url,data=data)

    @staticmethod
    def delete_employee(url):
        response = requests.delete(url)

class UserInput(Employee,Department):
    
    EMPLOYEE_URL    = 'http://127.0.0.1:8000/v1/employees/'
    DEPARTMENT_URL  = 'http://127.0.0.1:8000/v1/departments/'
    
    def __init__(self) -> None:
        self.get_user_input()

    def get_department_details(self):
        response   = Department.get_department(self.DEPARTMENT_URL )
        return response.text

    def get_user_input(self):
        while True:
            print('<---------------------EMPLOYEE DATABASE ------------------------------>')
            print("\n1 - Create  \t 2 - Read \t 3 - Update \t 4 - Delete \t 5 - Exit ")
            selection = int(input('\nEnter your selection : '))

            if selection == 1:
                print('\n1.ADD A NEW EMPLOYEE SECTION')
                emp_id      = int(input('a)Enter employee id(numeric values preferred) : ')) 
                emp_name    = input('b)Enter employee name : ')
                print(self.get_department_details())
                emp_dept    = int(input('c)Enter employee dept id(select it from above list) : '))
                response = Employee.add_employee(self.EMPLOYEE_URL,{"emp_id":emp_id,"emp_name":emp_name,"department":emp_dept})
                if response.status_code == 201:
                    print('Employee information has been added')
                else:
                    print('Error while adding employee info. Please try after sometime.')
            
            if selection == 2:
                print('\n2.GET EMPLOYEE INFORMATION BY ID')
                emp_id      = input('a)Enter employee id : ')
                response = Employee.get_employee(self.EMPLOYEE_URL+emp_id)
                if response.status_code == 200:
                    print(response.text)
                else:
                    print("Invalid Id")

            if selection == 3:
                print('\n3.UPDATE EMPLOYEE INFORMATION BY ID')
                emp_id      = input('a)Enter employee id : ')
                response = Employee.get_employee(self.EMPLOYEE_URL+emp_id)
                if response.status_code == 200:
                    emp_name    = input('b)Enter employee name : ')
                    print(self.get_department_details())
                    emp_dept    = int(input('c)Enter employee dept id(select it from above list) : '))
                    response = Employee.update_employee(self.EMPLOYEE_URL+emp_id,{"emp_id":emp_id,"emp_name":emp_name,"department":emp_dept})
                    if response.status_code == 200:
                        print('Employee information has been updated')
                    else:
                        print('Error while updating employee info.')
                else:
                    print("Invalid Id")

            if selection == 4:
                print('\n4.DELETE EMPLOYEE INFORMATION BY ID')
                emp_id      = input('a)Enter employee id : ')
                response = Employee.delete_employee(self.EMPLOYEE_URL+emp_id)
                if response.status_code == 204:
                    print('Employee information has deleted')
                else:
                    print("Invalid Id")
            
            if selection == 5 :
                exit()

if __name__ == "__main__":
    obj = UserInput()

import requests

class Employee():
    
    def __init__(self) -> None:
        pass

    def get_employee(self,url):
        response = requests.get(url)
        print(response.status_code)

    def add_employee(self,url,data):
        response = requests.post(url,data=data)
        print(response.status_code)

    def update_employee(self,url,data):
        response = requests.put(url,data=data)
        print(response.status_code)

    def delete_employee(self,url):
        response = requests.delete(url)
        print(response.status_code)

class Department():
    
    def __init__(self) -> None:
        pass

    def get_department(self,url):
        response = requests.get(url)
    
    def add_department(self,url,data):
        response = requests.post(url,data=data)

    def update_department(self,url,data):
        response = requests.put(url,data=data)

    def delete_employee(self,url):
        response = requests.delete(url)

class UserInput(Employee,Department):
    
    EMPLOYEE_URL    = 'http://127.0.0.1:8000/v1/employees/'
    DEPARTMENT_URL  = 'http://127.0.0.1:8000/v1/departments/'
    
    def __init__(self) -> None: 

        super().get_employee(self.EMPLOYEE_URL + str(112132))

if __name__ == "__main__":
    obj = UserInput()

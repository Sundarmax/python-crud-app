from django.db import models



class Department(models.Model):
    dept_id   = models.IntegerField(primary_key=True)
    dept_name = models.CharField(max_length=60)

class Employee(models.Model):
    emp_id      = models.IntegerField(primary_key=True)
    emp_name    = models.CharField(max_length=90)
    department  = models.OneToOneField(Department,related_name="employee_department",on_delete=models.CASCADE)

#a = Department(dept_id = 11,dept_name="InfoTech")
#obj = Department.objects.all()
#print(obj)

get_obj = Department.objects.get(dept_id=11)
new = Employee(emp_id = 1111,emp_name="A",department=get_obj)
new.save()
from django.urls import path
from django.conf.urls import url, include
from .views import Department,Employee,DepartmentById,EmployeeById

urlpatterns = [
    path('departments/', Department.as_view()),
    path('departments/<int:id>', DepartmentById.as_view()),
    path('employees/', Employee.as_view()),
    path('employees/<int:id>',EmployeeById.as_view())
]

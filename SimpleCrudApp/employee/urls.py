from django.urls import path
from django.conf.urls import url, include
from .views import Department,Employee,DepartmentById,EmployeeById

urlpatterns = [
    path('department/', Department.as_view()),
    path('department/<int:id>', DepartmentById.as_view()),
    path('employee/', Employee.as_view()),
    path('employee/<int:id>',EmployeeById.as_view())
]

from django.urls import path
from django.conf.urls import url, include
from .views import Department,Employee

urlpatterns = [
    path('departments/', Department.as_view()),
    path('employee/', Employee.as_view())
]

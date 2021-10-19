from django.urls import path
from django.conf.urls import url, include
from .views import Department

urlpatterns = [
    path('departments/', Department.as_view())
]

from .views import home, view_students
from django.urls import path

urlpatterns = [
    path('',home),
    path('viewstudents/', view_students),
]
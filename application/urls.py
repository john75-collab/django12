from .views import home, view_students, delete_student, edit_student
from django.urls import path

urlpatterns = [
    path('',home),
    path('viewstudents/', view_students),
    path('delete/<int:id>/', delete_student),
    path('edit/<int:id>/', edit_student),
]
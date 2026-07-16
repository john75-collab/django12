from django.urls import path
from .views import (
    login,
    register,
    student_page,
    view_students,
    delete_student,
    edit_student
)

urlpatterns = [
    path('', login),
    path('register/', register, name='register'),
    path('student/', student_page),
    path('viewstudents/', view_students),
    path('delete/<int:id>/', delete_student),
    path('edit/<int:id>/', edit_student),
]
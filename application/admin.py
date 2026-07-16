from django.contrib import admin
from .models import student, Login, Profile

admin.site.register(student)
admin.site.register(Login)
admin.site.register(Profile)
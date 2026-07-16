from django.db import models
from django.contrib.auth.models import User


# -------------------------------
# Student Model
# -------------------------------
class student(models.Model):

    sid = models.IntegerField()

    name = models.CharField(max_length=200)

    qualification = models.CharField(max_length=100)

    email = models.EmailField()

    phno = models.BigIntegerField()

    trainer = models.CharField(max_length=100)

    course = models.CharField(max_length=100)

    status = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# -------------------------------
# Login History Model
# -------------------------------
class Login(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    role = models.CharField(max_length=20)

    login_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


# -------------------------------
# User Profile Model
# -------------------------------
class Profile(models.Model):

    ROLE_CHOICES = [
        ('student', 'Student'),
        ('staff', 'Staff'),
        ('admin', 'Admin'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )

    def __str__(self):
        return self.user.username
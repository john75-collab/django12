from django.db import models

class student (models.Model):
    sid=models.IntegerField()
    name=models.CharField(max_length=200)
    qualification=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    phno=models.IntegerField()
    trainer=models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Login(models.Model):

    name = models.CharField(max_length=100)

    password = models.CharField(max_length=100)

    role = models.CharField(max_length=20)

    def __str__(self):
        return self.name
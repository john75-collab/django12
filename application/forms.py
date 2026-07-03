from django import forms 
class studentForm(forms.Form):
    sid=forms.IntegerField()
    name=forms.CharField(max_length=200)
    qualification=forms.CharField(max_length=100)
    email=forms.CharField(max_length=200)
    phno=forms.IntegerField()
    trainer=forms.CharField(max_length=100)
    course=forms.CharField(max_length=100)
    status=forms.CharField(max_length=100)
class LoginForm(forms.Form):

    name = forms.CharField(max_length=100)

    password = forms.CharField(widget=forms.PasswordInput())

    ROLE_CHOICES = [
        ('student', 'Student'),
        ('staff', 'Staff'),
        ('admin', 'Admin'),
    ]

    role = forms.ChoiceField(choices=ROLE_CHOICES)
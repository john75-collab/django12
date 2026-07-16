from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User

from .models import student, Login, Profile

from .forms import studentForm
from .forms import LoginForm
from .forms import RegisterForm

def student_page(request):

    if request.method == "POST":

        form = studentForm(request.POST)

        if form.is_valid():

            student.objects.create(
                sid=form.cleaned_data['sid'],
                name=form.cleaned_data['name'],
                qualification=form.cleaned_data['qualification'],
                email=form.cleaned_data['email'],
                phno=form.cleaned_data['phno'],
                trainer=form.cleaned_data['trainer'],
                course=form.cleaned_data['course'],
                status=form.cleaned_data['status']
            )

    form = studentForm()

    return render(
        request,
        'index.html',
        {
            'form': form,
            'role': request.session.get('role')
        }
    )


def view_students(request):

    students = student.objects.all()

    return render(
        request,
        'students.html',
        {
            'students': students,
            'role': request.session.get('role')
        }
    )
def delete_student(request, id):

    role = request.session.get('role')

    if role != 'admin':
        return redirect('/student/')

    data = student.objects.get(id=id)

    data.delete()

    return redirect('/viewstudents/')
def edit_student(request, id):

    role = request.session.get('role')

    if role not in ['staff', 'admin']:
        return redirect('/student/')

    data = student.objects.get(id=id)

    if request.method == "POST":

        data.sid = request.POST['sid']
        data.name = request.POST['name']
        data.qualification = request.POST['qualification']
        data.email = request.POST['email']
        data.phno = request.POST['phno']
        data.trainer = request.POST['trainer']
        data.course = request.POST['course']
        data.status = request.POST['status']

        data.save()

        return redirect('/viewstudents/')

    return render(
        request,
        'edit.html',
        {'student': data}
    )
def login(request):

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['name']
            password = form.cleaned_data['password']

            # Authenticate user
            user = authenticate(
                username=username,
                password=password
            )

            if user is not None:

                auth_login(request, user)

                # Get role from Profile table
                profile = Profile.objects.get(user=user)

                print("Logged in user:", user.username)
                print("Profile role:", profile.role)

                request.session['role'] = profile.role

                print("Session role:", request.session['role'])

                # Save login history
                Login.objects.create(
                    user=user,
                    role=profile.role
                )

                # Store session
                request.session['role'] = profile.role
                request.session['name'] = user.first_name

                return redirect('/student/')

            else:

                return render(
                    request,
                    "login.html",
                    {
                        "form": form,
                        "error": "Invalid Username or Password"
                    }
                )

    return render(request, "login.html", {"form": form})
def register(request):

    form = RegisterForm()

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            name = form.cleaned_data['name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']

            # Create Django User
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=name
            )

            # Save role
            Profile.objects.create(
                user=user,
                role=role
            )

            return redirect('/')

    return render(
        request,
        'register.html',
        {'form': form}
    )
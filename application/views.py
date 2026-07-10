from django.shortcuts import render, redirect
from .forms import studentForm
from .models import student, Login
from .forms import LoginForm

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

            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']

            Login.objects.create(
                name=name,
                password=password,
                role=role
            )

            request.session['role'] = role
            request.session['name'] = name

            return redirect('/student/')

    return render(request, "login.html", {"form": form})
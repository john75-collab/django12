from django.shortcuts import render
from .forms import studentForm
from .models import student

def home(request):

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

    return render(request, 'index.html', {'form': form})


def view_students(request):

    students = student.objects.all()

    return render(
        request,
        'students.html',
        {'students': students}
    )
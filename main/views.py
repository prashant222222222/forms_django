from django.shortcuts import render
from main import forms, models
from django.shortcuts import HttpResponseRedirect
# Create your views here.


def index(request):
    # forms are not included on dhango by default
    context = {
        "form": forms.example
    }
    return render(request, 'index.html', context)


def students(request):
    students = models.Student.objects.all()
    context = {
        "students": students
    }
    return render(request, 'students.html', context)


def addstudent(request):
    studentform = forms.StudentForm()
    # if request.method == "GET":
    # studentform=forms.StudentForm()
    # else:
    # data={
    # "name":request.POST["name"] //not sanitize data
    # }    not good method to retain data in form ,

    if request.method == "POST":
        studentform = forms.StudentForm(request.POST)
        if studentform.is_valid():
            student = studentform.save()  # creates new instancae for the model
            return HttpResponseRedirect('/students')
    context = {
        "studentform": studentform
    }
    return render(request, 'addstudent.html', context)

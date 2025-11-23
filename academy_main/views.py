from django.http import HttpResponse
from academy.models import Course, Trainer, Student
from django.shortcuts import render


def home(request):
    courses = Course.objects.all()
    trainers = Trainer.objects.all()
    students = Student.objects.all()
    courses_count = courses.count()
    trainers_count = trainers.count()
    students_count = students.count()

    context = {
        'courses': courses,
        'trainers': trainers,
        'students': students,
        'courses_count': courses_count,
        'trainers_count': trainers_count,
        'students_count': students_count
    }
    return render(request, 'home.html', context)
    # return HttpResponse("Welcome to the Training Portal Home Page!")


def courses(request):
    courses = Course.objects.all()
    print(courses)
    context = {
        'courses': courses,
    }
    return render(request, 'courses.html', context)


def trainers(request):
    trainers = Trainer.objects.all()
    context = {
        'trainers': trainers,
    }
    return render(request, 'trainers.html', context)


def students(request):
    students = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'students.html', context)

from django.http import HttpResponse
from academy.models import Course, Trainer, Student
from django.shortcuts import render, get_object_or_404
from academy.forms import StudentForm, TrainerForm, CourseForm
from django.contrib.auth.decorators import login_required, permission_required


# Views for the Home Page
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

# Views for Course Management
def courses(request):
    courses = Course.objects.all()
    print(courses)
    context = {
        'courses': courses,
    }
    return render(request, 'courses.html', context)


def course_detail(request, id):
    course = get_object_or_404(Course, pk=id)
    context = {
        'course': course,
    }
    return render(request, 'course_detail.html', context)


@login_required
@permission_required('academy.change_course', raise_exception=True)
def edit_course(request, id):
    course = get_object_or_404(Course, pk=id)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            context = {
                'message': "Course updated successfully."
            }
            return render(request, 'success_message.html', context)
        else:
            print(form.errors)

    form = CourseForm(instance=course)
    context = {
        'form': form,
        'course': course,
    }
    return render(request, 'edit_course.html', context)


@login_required
@permission_required('academy.delete_course', raise_exception=True)
def delete_course(request, id):
    course = get_object_or_404(Course, pk=id)
    course.delete()
    context = {
        'message': "Course deleted successfully."
    }
    return render(request, 'success_message.html', context)


@login_required
@permission_required('academy.add_course', raise_exception=True)
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context = {
                'message': "Course added successfully."
            }
            return render(request, 'success_message.html', context)
        else:
            print(form.errors)

    form = CourseForm()
    context = {
        'form': form
    }
    return render(request, 'add_course.html', context)


# Views for Trainer Management
def trainers(request):
    trainers = Trainer.objects.all()
    context = {
        'trainers': trainers,
    }
    return render(request, 'trainers.html', context)


@login_required
def trainer_detail(request, id):
    trainer = get_object_or_404(Trainer, pk=id)
    context = {
        'trainer': trainer,
    }
    return render(request, 'trainer_detail.html', context)


@login_required
@permission_required('academy.change_trainer', raise_exception=True)
def edit_trainer(request, id):
    trainer = get_object_or_404(Trainer, pk=id)
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES, instance=trainer)
        if form.is_valid():
            form.save()
            context = {
                'message': "Trainer updated successfully."
            }
            return render(request, 'success_message.html', context)
        else:
            print(form.errors)

    form = TrainerForm(instance=trainer)
    context = {
        'form': form,
        'trainer': trainer,
    }
    return render(request, 'edit_trainer.html', context)


@login_required
@permission_required('academy.delete_trainer', raise_exception=True)
def delete_trainer(request, id):
    trainer = get_object_or_404(Trainer, pk=id)
    trainer.delete()
    context = {
        'message': "Trainer deleted successfully."
    }
    return render(request, 'success_message.html', context)


@login_required
@permission_required('academy.add_trainer', raise_exception=True)
def add_trainer(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context = {
                'message': "Trainer added successfully."
            }
            return render(request, 'success_message.html', context)
        else:
            print(form.errors)

    form = TrainerForm()
    context = {
        'form': form
    }
    return render(request, 'add_trainer.html', context)


# Views for Student Management
def students(request):
    students = Student.objects.all()
    context = {
        'students': students,
    }
    return render(request, 'students.html', context)


@login_required
@permission_required('academy.view_student', raise_exception=True)
def student_detail(request, id):
    student = get_object_or_404(Student, pk=id)
    context = {
        'student': student,
    }
    return render(request, 'student_detail.html', context)


@login_required
@permission_required('academy.add_student', raise_exception=True)
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context = {
                'message': "Student added successfully."
            }
            return render(request, 'success_message.html', context)
        else:
            print(form.errors)

    form = StudentForm()
    context = {
        'form': form
    }
    return render(request, 'add_student.html', context)


@login_required
@permission_required('academy.change_student', raise_exception=True)
def edit_student(request, id):
    student = get_object_or_404(Student, pk=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            context = {
                'message': "Student updated successfully."
            }
            return render(request, 'success_message.html', context)
        else:
            print(form.errors)

    form = StudentForm(instance=student)
    context = {
        'form': form,
        'student': student,
    }
    return render(request, 'edit_student.html', context)


@login_required
@permission_required('academy.delete_student', raise_exception=True)
def delete_student(request, id):
    student = get_object_or_404(Student, pk=id)
    student.delete()
    context = {
        'message': "Student deleted successfully."
    }
    return render(request, 'success_message.html', context)

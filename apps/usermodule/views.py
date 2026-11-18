from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404

from .models import Address, Student, Student2
from .forms import StudentForm, Student2Form


def students_per_city(request):
    cities = Address.objects.annotate(num_students=Count('student'))
    return render(request, 'usermodule/students_per_city.html', {'cities': cities})


def lab11_task1_students(request):
    students = Student.objects.all().order_by('-id')
    return render(request, 'usermodule/lab11_task1/students.html', {'students': students})


def lab11_task1_addstudent(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users.lab11_task1_students')
    else:
        form = StudentForm()
    return render(request, 'usermodule/lab11_task1/addstudent.html', {'form': form})


def lab11_task1_editstudent(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('users.lab11_task1_students')
    else:
        form = StudentForm(instance=student)
    return render(request, 'usermodule/lab11_task1/editstudent.html', {'form': form, 'student': student})


def lab11_task1_deletestudent(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('users.lab11_task1_students')


def lab11_task2_students(request):
    students = Student2.objects.all().order_by('-id')
    return render(request, 'usermodule/lab11_task2/students.html', {'students': students})


def lab11_task2_addstudent(request):
    if request.method == 'POST':
        form = Student2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users.lab11_task2_students')
    else:
        form = Student2Form()
    return render(request, 'usermodule/lab11_task2/addstudent.html', {'form': form})


def lab11_task2_editstudent(request, id):
    student = get_object_or_404(Student2, id=id)
    if request.method == 'POST':
        form = Student2Form(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('users.lab11_task2_students')
    else:
        form = Student2Form(instance=student)
    return render(request, 'usermodule/lab11_task2/editstudent.html', {'form': form, 'student': student})


def lab11_task2_deletestudent(request, id):
    student = get_object_or_404(Student2, id=id)
    student.delete()
    return redirect('users.lab11_task2_students')

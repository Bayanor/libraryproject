from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404

from .models import Address, Student, Student2
from .forms import StudentForm, Student2Form, SignUpForm, LoginForm


def students_per_city(request):
    cities = Address.objects.annotate(num_students=Count('student'))
    return render(request, 'usermodule/students_per_city.html', {'cities': cities})


@login_required
def lab11_task1_students(request):
    students = Student.objects.all().order_by('-id')
    return render(request, 'usermodule/lab11_task1/students.html', {'students': students})


@login_required
def lab11_task1_addstudent(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users.lab11_task1_students')
    else:
        form = StudentForm()
    return render(request, 'usermodule/lab11_task1/addstudent.html', {'form': form})


@login_required
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


@login_required
def lab11_task1_deletestudent(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('users.lab11_task1_students')


@login_required
def lab11_task2_students(request):
    students = Student2.objects.all().order_by('-id')
    return render(request, 'usermodule/lab11_task2/students.html', {'students': students})


@login_required
def lab11_task2_addstudent(request):
    if request.method == 'POST':
        form = Student2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users.lab11_task2_students')
    else:
        form = Student2Form()
    return render(request, 'usermodule/lab11_task2/addstudent.html', {'form': form})


@login_required
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


@login_required
def lab11_task2_deletestudent(request, id):
    student = get_object_or_404(Student2, id=id)
    student.delete()
    return redirect('users.lab11_task2_students')


def lab12_register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'You have successfully registered, ' + user.username + '.')
            return redirect('users.login')
        messages.error(request, 'An error occurred while saving the data.')
    else:
        form = SignUpForm()
    return render(request, 'usermodule/lab12/register.html', {'form': form})


def lab12_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request,
                                username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)  # stores the session in the request
                messages.success(request, 'Login successfully.')
                return redirect(request.GET.get('next') or 'books.index')
            messages.error(request, 'Wrong username or password.')
        else:
            messages.error(request, 'An error occurred while reading the form.')
    else:
        form = LoginForm()
    return render(request, 'usermodule/lab12/login.html', {'form': form})


def lab12_logout(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('books.index')  # goto landing page

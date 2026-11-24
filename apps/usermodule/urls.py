from django.urls import path

from . import views

urlpatterns = [
    path('lab8/task7', views.students_per_city, name="users.lab8_task7"),

    path('lab11_task1/students', views.lab11_task1_students, name="users.lab11_task1_students"),
    path('lab11_task1/addstudent', views.lab11_task1_addstudent, name="users.lab11_task1_addstudent"),
    path('lab11_task1/editstudent/<int:id>', views.lab11_task1_editstudent, name="users.lab11_task1_editstudent"),
    path('lab11_task1/deletestudent/<int:id>', views.lab11_task1_deletestudent, name="users.lab11_task1_deletestudent"),

    path('lab11_task2/students', views.lab11_task2_students, name="users.lab11_task2_students"),
    path('lab11_task2/addstudent', views.lab11_task2_addstudent, name="users.lab11_task2_addstudent"),
    path('lab11_task2/editstudent/<int:id>', views.lab11_task2_editstudent, name="users.lab11_task2_editstudent"),
    path('lab11_task2/deletestudent/<int:id>', views.lab11_task2_deletestudent, name="users.lab11_task2_deletestudent"),

    path('register', views.lab12_register, name="users.register"),
    path('login', views.lab12_login, name="users.login"),
    path('logout', views.lab12_logout, name="users.logout"),
]

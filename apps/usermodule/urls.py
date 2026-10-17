from django.urls import path

from . import views

urlpatterns = [
    path('lab8/task7', views.students_per_city, name="users.lab8_task7"),
]

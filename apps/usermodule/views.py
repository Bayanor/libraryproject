from django.db.models import Count
from django.shortcuts import render

from .models import Address


def students_per_city(request):
    cities = Address.objects.annotate(num_students=Count('student'))
    return render(request, 'usermodule/students_per_city.html', {'cities': cities})

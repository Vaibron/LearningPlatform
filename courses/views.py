from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from . import models
from .models import Course


# Create your views here.

def course_main_page(request):
    courses = Course.objects.all()  # Получаем все курсы из базы данных
    context = {'courses': courses}
    return render(request, 'courses.html', context)

def single_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    context = {'course': course}
    return render(request, 'single_course.html', context)
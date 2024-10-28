from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_main_page, name='course_list'),  # Измените имя на 'course_list'
    path('<int:course_id>/', views.single_course, name='single_course')
]
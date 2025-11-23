from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('', views.home, name='home'),
    path('academy/courses/', views.courses, name='academy_courses'),
    path('academy/trainers/', views.trainers, name='academy_trainers'),
    path('academy/students/', views.students, name='academy_students'),
]

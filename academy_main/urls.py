from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from accounts import views as accounts_views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('courses/', views.courses, name='academy_courses'),
    path('courses/<int:id>/', views.course_detail, name='course_detail'),
    path('courses/edit/<int:id>/', views.edit_course, name='edit_course'),
    path('courses/delete/<int:id>/', views.delete_course, name='delete_course'),
    path('courses/add/', views.add_course, name='add_course'),
    path('trainers/', views.trainers, name='academy_trainers'),
    path('trainers/<int:id>/', views.trainer_detail, name='trainer_detail'),
    path('trainers/edit/<int:id>/', views.edit_trainer, name='edit_trainer'),
    path('trainers/delete/<int:id>/', views.delete_trainer, name='delete_trainer'),
    path('trainers/add/', views.add_trainer, name='add_trainer'),
    path('students/', views.students, name='academy_students'),
    path('students/<int:id>/', views.student_detail, name='student_detail'),
    path('students/edit/<int:id>/', views.edit_student, name='edit_student'),
    path('students/delete/<int:id>/', views.delete_student, name='delete_student'),
    path('students/add/', views.add_student, name='add_student'),
    path("register/", accounts_views.register, name="register"),
    path("login/", accounts_views.login, name="login"),
    path("logout/", accounts_views.logout, name="logout"),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)

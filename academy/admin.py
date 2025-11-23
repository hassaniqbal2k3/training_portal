from django.contrib import admin
from .models import Course, Trainer, Student


class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'duration_in_weeks', 'course_image')
    search_fields = ('course_name',)
    list_filter = ('duration_in_weeks',)


class TrainerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'expertise', 'trainer_photo')
    search_fields = ('first_name', 'last_name', 'expertise')
    list_filter = ('expertise',)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'is_active',
                    'enrolled_course', 'enrolled_trainer')
    list_filter = ('is_active', 'enrolled_course', 'enrolled_trainer')
    search_fields = ('first_name', 'last_name', 'email')
    readonly_fields = ('enrolled_course', 'enrolled_trainer')
    

# Register your models here.


admin.site.register(Trainer, TrainerAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)

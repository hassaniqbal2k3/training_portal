from django.db import models

# Create your models here.


class Course(models.Model):
    course_name = models.CharField(max_length=200)
    description = models.TextField()
    duration_in_weeks = models.IntegerField()
    course_image = models.ImageField(
        upload_to='course_images/', default='default.png')

    def __str__(self):
        return self.course_name


class Trainer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    expertise = models.TextField(blank=True)
    trainer_photo = models.ImageField(
        upload_to='trainer_photos/', default='default.png')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_photo = models.ImageField(
        upload_to='student_photos/', default='default.png')
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    enrolled_course = models.ForeignKey(
        Course, on_delete=models.CASCADE, null=True, blank=True)
    enrolled_trainer = models.ForeignKey(
        Trainer, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

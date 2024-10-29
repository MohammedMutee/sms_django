from django.db import models

# Create your models here.
from django.db import models
from adminapp.models import StudentList

class AddCourse(models.Model):
    COURSE_CHOICE = [
        ('AOOP', 'Advanced Object Oriented Programming'),
        ('PFSD', 'Python Full Stack Development'),
    ]
    SECTION_CHOICE = [
        ('S11', 'Section S11'),
        ('S12', 'Section S12'),
        ('S13', 'Section S13'),
    ]

    student = models.ForeignKey(StudentList, on_delete=models.CASCADE)
    course = models.CharField(max_length=50, choices=COURSE_CHOICE)
    section = models.CharField(max_length=50, choices=SECTION_CHOICE)

    def __str__(self):
        return f'{self.student.Register_Number} - {self.course} ({self.section})'

class Marks(models.Model):
    COURSE_CHOICE = [
        ('AOOP', 'Advanced Object Oriented Programming'),
        ('PFSD', 'Python Full Stack Developments'),
    ]
    student = models.ForeignKey(StudentList, on_delete=models.CASCADE)
    course = models.CharField(max_length=50, choices=COURSE_CHOICE)
    marks = models.IntegerField()
    def __str__(self):
        return f"{self.student.name} - {self.course}"
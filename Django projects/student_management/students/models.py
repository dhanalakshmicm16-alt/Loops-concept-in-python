from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='marks')
    subject = models.CharField(max_length=100)
    marks = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.student.name} - {self.subject}: {self.marks}"

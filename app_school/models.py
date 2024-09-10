from django.db import models

class Subject(models.Model):
    subject_name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.subject_name
    
class Teacher(models.Model):
    teacher_name = models.CharField(max_length=100)
    teacher_surname = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.teacher_name} {self.teacher_surname}'
    
class Class(models.Model):
    class_name = models.CharField(max_length=100, unique=True)
    year = models.IntegerField()

    def __str__(self):
        return self.class_name
    
class Student(models.Model):
    student_name = models.CharField(max_length=100)
    student_surname = models.CharField(max_length=100)
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.student_name} {self.student_surname}'
    
class Schedule(models.Model):
    schedule_name = models.CharField(max_length=10)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

class Grade(models.Model):
    grade = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

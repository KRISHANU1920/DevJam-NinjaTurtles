from django.db import models

# Create your models here.
class PYQ(models.Model):
    Qid = models.AutoField
    course = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    semester = models.CharField(max_length=50)
    exam = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    file = models.FileField(upload_to="academics/PYQ")
    date = models.DateField()

    def __str__(self):
        return self.subject

class Book(models.Model):
    Bid = models.AutoField
    Dept = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    Name = models.CharField(max_length=50)
    Author = models.CharField(max_length=50)
    file = models.FileField(upload_to="academics/Book")
    date = models.DateField()

    def __str__(self):
        return self.Name

class TimeTable(models.Model):
    Tid = models.AutoField
    course = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    semester = models.CharField(max_length=50)
    file = models.FileField(upload_to="academics/TimeTable")
    date = models.DateField()

    def __str__(self):
        return self.course

class Calender(models.Model):
    Cid = models.AutoField
    course = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    semester = models.CharField(max_length=50)
    file = models.FileField(upload_to="academics/Calender")
    date = models.DateField()

    def __str__(self):
        return self.course

class Assignment(models.Model):
    Aid = models.AutoField
    course = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    Semester = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    file = models.FileField(upload_to="academics/Assignment")
    date = models.DateField()

    def __str__(self):
        return self.subject
from django.db import models
from django.utils import timezone

class Lab(models.Model):
    intro = models.TextField()
    BSpro = models.CharField(max_length=200)
    MSpro = models.CharField(max_length=200)

    def __str__(self):
        self.intro

class Professor(models.Model):
    kname = models.CharField(max_length=20)
    ename = models.CharField(max_length=30)
    state = models.CharField(max_length=200, default=".")
    organization = models.CharField(max_length=200)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    image = models.ImageField(upload_to="web/posts/title/image", default="/dd")

    def __str__(self):
        return self.kname

class Education(models.Model):
    degree = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    date = models.CharField(max_length=200)

    def __str__(self):
        return self.degree

class Experience(models.Model):
    content = models.CharField(max_length=200)
    date = models.CharField(max_length=200)

    def __str__(self):
        return self.content

class Lecture(models.Model):
    time = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    grade = models.CharField(max_length=200)

    def __str__(self):
        return self.course

class Member(models.Model):
    kname = models.CharField(max_length=20)
    ename = models.CharField(max_length=30)
    degree = models.CharField(max_length=20, default="BS Student")
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    image = models.ImageField(upload_to="web/members/image", default="web/members/image/base.jpg")
    graduated = models.BooleanField()
    company = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.kname
class Link(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200, default='', blank=True)
    test = models.CharField(max_length=200, default='')
    def __str__(self):
        return self.title
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Publication(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    journal = models.CharField(max_length=200)
    date = models.CharField(max_length=200, default='')
    link = models.CharField(max_length=200, default='',null=True)
    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    cost = models.CharField(max_length=200)

    def __str__(self):
        return self.title


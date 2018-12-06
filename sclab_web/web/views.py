from django.shortcuts import render
from .models import *
from django.db.models import Count

# Create your views here.
def index(request):
    news = Post.objects.all().order_by('-id')
    return render(request, 'web/index.html', {'news' : news})

def professor(request):
    professors = Professor.objects.all()
    educations = Education.objects.all().order_by('-id')
    experiences = Experience.objects.all().order_by('-id')
    lectures = Lecture.objects.all()
    return render(request, 'web/professor.html', {'professors' : professors, 'educations' : educations, 'experiences' : experiences, 'lectures' : lectures})

def members(request):
    currents = Member.objects.filter(graduated=False).order_by('-degree')
    graduates = Member.objects.filter(graduated=True).exclude(company__isnull=True).exclude(company="").order_by('-degree')
    return render(request, 'web/members.html', {'currents' : currents, 'graduates' : graduates})

def location(request):
    return render(request,'web/location.html')

def news(request):
    news = New.objects.all().order_by('-id')
    return render(request, 'web/news.html', {'news' : news})

def posts(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'web/post.html', {'post' : post})

def publication(request):
    publications = Publication.objects.values('date').annotate(Count('date'))
    for pub in publications:
        d = dict()
        d['pub'] = Publication.objects.filter(date=pub['date'])
        pub.update(d)
    return render(request, 'web/publication.html', {'publications' : publications[::-1]})

def project(request):
    projects = Project.objects.all().order_by('-id')
    return render(request, 'web/project.html', {'projects' : projects})

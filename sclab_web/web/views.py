from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, 'web/index.html')

def professor(request):
    return render(request, 'web/professor.html')

def members(request):
    currents = Member.objects.filter(graduated=False).order_by('-degree')
    graduates = Member.objects.filter(graduated=True).exclude(company__isnull=True).exclude(company="").order_by('-degree')
    return render(request, 'web/members.html', {'currents' : currents, 'graduates' : graduates})

def news(request):
    news = Post.objects.all()
    return render(request, 'web/news.html', {'news' : news})

def publication(request):
    publications = Publication.objects.all()
    return render(request, 'web/publication.html', {'publications' : publications})

def project(request):
    projects = Project.objects.all()
    return render(request, 'web/project.html', {'projects' : projects})

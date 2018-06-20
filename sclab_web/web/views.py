from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'web/index.html')

def professor(request):
    return render(request, 'web/professor.html')

def members(request):
    return render(request, 'web/members.html')

def news(request):
    return render(request, 'web/news.html')

def publication(request):
    return render(request, 'web/publication.html')

def project(request):
    return render(request, 'web/project.html')

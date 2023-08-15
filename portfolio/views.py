from django.shortcuts import render
from .models import Service, Skills,Exp, Projects
# Create your views here.
def home(request):
    projects = Projects.objects.all()
    exp = Exp.objects.all()
    skills = Skills.objects.all()
    services = Service.objects.all()
    return render(request, "portfolio/index.html", {'services': services, 'skills': skills,
                                                    'exp' : exp, 'projects' : projects})
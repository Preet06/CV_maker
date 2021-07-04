from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

from django.template.loader import get_template
from django.http import HttpResponse
from io import StringIO
from django.template.loader import get_template 
from django.template import Context 

# Create your views here.
def home(request):
    return render(request, 'home.html')

def style(request):
    return render(request, 'style.html')


def input(request):
    return render(request, 'input.html')

def style1(request):
    if request.method == 'GET':
        Name = request.GET.get('Name')
        Email_ID = request.GET.get('Email_ID')
        Achievements = request.GET.get('Achievements')
        Carrier_Goal = request.GET.get('Carrier_Goal')
        Skills = request.GET.get('Skills')
        context = {
        "Name": Name,
        "Email_ID": Email_ID,
        "Achievements": Achievements,
        "Carrier_Goal": Carrier_Goal,
        "Skills": Skills,
         }
    return render(request, 'style1.html', context)       






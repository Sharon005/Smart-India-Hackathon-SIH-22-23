from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    return render(request, 'Web_App/index.html')

def crops(request):
    return render(request, 'Web_App/crops.html')

def meetings(request):
    return render(request, 'Web_App/meetings.html')

def meeting_d(request):
    return render(request, 'Web_App/meeting-details.html')
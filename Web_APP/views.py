from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
import joblib

# Create your views here.

def home(request):
    return render(request, 'Web_App/index.html')

def crops(request):
    return render(request, 'Web_App/crops.html')

def disease(request):
    return render(request, 'Web_App/disease.html')

def crop_result(request):

    cls = joblib.load('finalized_model.sav')

    lis = []

    lis.append(request.GET['N'])
    lis.append(request.GET['P'])
    lis.append(request.GET['K'])
    lis.append(request.GET['Temperature'])
    lis.append(request.GET['Humiditiy'])
    lis.append(request.GET['Ph'])
    lis.append(request.GET['Rainfall'])

    ans = cls.predict([lis])


    return render(request, 'Web_App/crop_result.html', {'ans':ans})

class WheatDView(ListView):
    model = Wheat_Disease

class WheatView(DetailView):
    model = Wheat_Disease

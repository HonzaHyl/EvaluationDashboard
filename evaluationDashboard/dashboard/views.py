from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import UploadTableForm, FileSelectForm

from .models import UploadTable

from django.urls import reverse

import pandas as pd


# Create your views here.

def index(request):
    data = []
    header = []

    if request.method == "POST":
        form = FileSelectForm(request.POST)
        if form.is_valid():
            fileName = form.cleaned_data['fileName']

            filePath = "media/" + fileName

            df = pd.read_csv(filePath, nrows=30, sep="\t")

            header = df.columns.tolist()
            data = df.values.tolist()

            context = {"data":data,
                "form":form,
               "header":header,}

            return render(request,'dashboard/index.html', context)
        
    form = FileSelectForm()
    context = {"data":data,
               "header":header,
               "form":form,
               }

    return render(request,'dashboard/index.html', context)

def load_file(request):
    if request.method == 'POST':
        form = UploadTableForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('dashboard:index'))
    else:        
        form = UploadTableForm()
        context = {'form':form,}
    return render(request,'dashboard/loadFile.html', context)

def graphs(request):
    if request.method == "POST":
        form = FileSelectForm(request.POST)
        if form.is_valid():
            fileName = form.cleaned_data['fileName']

            context = {
                "form":form,
                }

            return render(request,'dashboard/graphs.html', context)
            
    form = FileSelectForm()
    context = {
         "form":form,
        }
    return render(request, 'dashboard/graphs.html', context)

def statistics(request):
      
    if request.method == "POST":
        form = FileSelectForm(request.POST)
        if form.is_valid():
            fileName = form.cleaned_data['fileName']

            context = {
                "form":form,
                }

            return render(request,'dashboard/statistics.html', context)
            
    form = FileSelectForm()
    context = {
         "form":form,
        }
    return render(request, 'dashboard/statistics.html', context)


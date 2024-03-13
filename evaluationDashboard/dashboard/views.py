from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import UploadTableForm

from django.urls import reverse

import pandas as pd


# Create your views here.

def index(request):
    filePath = "media/documents/merged_genefamilies_tables.tsv"
    data = []

    df = pd.read_csv(filePath, nrows=30, sep="\t", header=None)

    data = df.values.tolist()
    context = {"data":data}

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

def genefamilies(request):
    return render(request, 'dashboard/genefamilies.html')
        
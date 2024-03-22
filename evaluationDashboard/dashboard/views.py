from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import UploadTableForm, FileSelectForm

from .models import UploadTable

from django.urls import reverse

import pandas as pd


# Create your views here.

def index(request):
    filePath = "media/documents/merged_genefamilies_tables.tsv"
    data = []

    df = pd.read_csv(filePath, nrows=30, sep="\t")

    header = df.columns.tolist()
    data = df.values.tolist()

    h = 0

    if request.method == "POST":
        form = FileSelectForm(request.POST)
        if form.is_valid():
            h = form.cleaned_data['fileName']

            context = {"data":data,
                "form":form,
               "header":header,
               "h":h}

            return render(request,'dashboard/index.html', context)
        
    form = FileSelectForm()
    context = {"data":data,
               "header":header,
               "form":form,
               "h":h}

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
    
    uploaded_files = UploadTable.objects.all()
    

    
    return render(request, 'dashboard/genefamilies.html', {'uploaded_files': uploaded_files})


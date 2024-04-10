# Import url and rendering stuff
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.template.loader import render_to_string
from django.http import JsonResponse

# Import forms
from .forms import UploadTableForm, FileSelectForm, UploadTSVForm

# Import models
from .models import UploadTSV

# Import data processing stuff
import pandas as pd

# Import pagination
from django.core.paginator import Paginator

import json
import csv


# Main page view

class index(View):
    template = 'dashboard/index.html'
 


    def get(self, request):
            
                return render(request, self.template)
            

class load_data(View):
    
    def get(self, request):
        if ('selectedFile' in request.session):
            filePath = request.session['selectedFile']

            # Read header of the tsv
            header = pd.read_csv(filePath, nrows=0, sep="\t")

            # Read the rest of available data
            df = pd.read_csv(filePath, sep="\t", index_col=0, header=0)

            # Extract header data to list
            header = header.columns.tolist()

            # Extract the rest of the data to list 
            data = df.to_csv()
            dict_data = []

            with open(filePath, "r") as table:
                reader = csv.DictReader(table, delimiter="\t")
                for row in reader:
                    dict_data.append(row)
                json_file = json.dumps(dict_data)

            context = {"values":dict_data}
                
            return JsonResponse(context)
        else:
            return JsonResponse({"header":"File not found"})



class load_file(View):
    #formClass = UploadTableForm
    formClass = UploadTSVForm
    template = "dashboard/loadFile.html"
    model = UploadTSV

    def get(self, request):
        context = {"form":self.formClass}
        return render(request, self.template, context)
    
    def post(self, request):
        form = self.formClass(request.POST, request.FILES)
        if form.is_valid():
            df = pd.read_csv(request.FILES['file'], sep="\t")
            json_file = df.to_json(orient="records")
            instance = UploadTSV(data=json_file)
            instance.save()
            return HttpResponseRedirect(reverse('dashboard:index'))
        

class select_file(View):
    formClass = FileSelectForm
    template = 'dashboard/selectFile.html'

    def get(self, request):
        context = {"form":self.formClass}
        return render(request, self.template, context)
    
    def post(self, request):
        form = self.formClass(request.POST)
        if form.is_valid():
            fileName = form.cleaned_data['fileName']
            filePath = 'media/' + fileName
            request.session['selectedFile'] = filePath
            return HttpResponseRedirect(reverse('dashboard:index')) 

class graphs(View):
    
    def get(self, request):

        return render(request, 'dashboard/graphs.html')


class statistics(View):
    def get(self, request):
        
        return render(request, 'dashboard/statistics.html')


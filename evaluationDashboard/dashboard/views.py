# Import url and rendering stuff
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import View

# Import forms
from .forms import UploadTableForm, FileSelectForm

# Import data processing stuff
import pandas as pd

# Import pagination
from django.core.paginator import Paginator


# Main page view

class index(View):
    template = 'dashboard/index.html'
    formClass = FileSelectForm


    def get(self, request):
            
            if ('selectedFile' in request.session):
                filePath = request.session['selectedFile']

                # Read header of the tsv
                header = pd.read_csv(filePath, nrows=0, sep="\t")

                # Read the rest of available data
                df = pd.read_csv(filePath, sep="\t",)

                # Extract header data to list
                header = header.columns.tolist()

                # Extract the rest of the data to list 
                data = df.to_numpy().tolist()

                # Set up pagination
                p = Paginator(data, 30)
                page = request.GET.get("page")

                selectedData = p.get_page(page)               
                
                context = {"selectedData":selectedData,
                "form":self.formClass,
               "header":header,}
                
                return render(request, self.template, context)

            else:
                context = {'selectedData':'',
                    'header':'',
                    'form':self.formClass,
                  }
                return render(request, self.template, context)


class load_file(View):
    formClass = UploadTableForm
    template = "dashboard/loadFile.html"

    def get(self, request):
        context = {"form":self.formClass}
        return render(request, self.template, context)
    
    def post(self, request):
        form = self.formClass(request.POST, request.FILES)
        if form.is_valid():
            form.save()
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


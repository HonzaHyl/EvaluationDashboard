from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import UploadTableForm

from django.urls import reverse


# Create your views here.

def index(request):
    return render(request,'dashboard/index.html')

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
        
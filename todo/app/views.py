from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

def index1(request):
    tasks=lists.objects.all()
    if request.method == 'POST':
        tasks=request.POST['task']
        data=lists.objects.create(tasks=tasks)
        data.save()
    return render(request,'index1.html',{'tasks':tasks})

def index2(request):
    tasks = lists.objects.all()
    return render(request,'index2.html',)

# Create your views here.

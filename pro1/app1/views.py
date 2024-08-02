from django.shortcuts import render
from.models import reviewModel
from.forms import *
# Create your views here.

def homeView(request):
    return render (request,"base.html",{})

def addview(request):
    form =reviewModelForm()
    if request.method=="POST":
        form=reviewModelForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,"app1/add.html",{"form":form})

def showView(request):
    obj=reviewModel.object.all()
    print(obj)
    return render (request,"app1/show.html",{"obj":obj})

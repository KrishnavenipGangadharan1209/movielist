from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import *
from .forms import *
from django.forms import ModelForm
# Create your views here.
def home(request):
    movie=movlist.objects.all()
    context={
        'movilist':movie
    }
    return render(request,'index.html',context)

def detail(request,movie_id):
    movie=movlist.objects.get(id=movie_id)
    return render(request,'details.html',{'movie':movie} )

def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('m_name')
        desc = request.POST.get('m_desc')
        ryear = request.POST.get('re_year')
        img = request.FILES['m_img']
        dir = request.POST.get('m_dir')
        movie=movlist(moviename=name,moviedisc=desc,Releaseyear=ryear,director=dir,poster=img)
        movie.save()
        return render(request,'index.html')

    return  render(request,'add.html')

def updatedata(request,id):
    movie=movlist.objects.get(id=id)
    form=movieform(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})

def delete(request,id):

    if request.method=='POST':

         movie=movlist.objects.get(id=id)
         movie.delete()
         return redirect('/')
    return render(request,'delete.html')


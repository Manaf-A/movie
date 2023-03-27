from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import movie
from . forms import movieform

# Create your views here.
def index(request):
    Movie=movie.objects.all()
    context={'movie_list':Movie}
    return render(request,'index.html',context)
def details(request,movie_id):
    Movie=movie.objects.get(id=movie_id)
    return render(request,'details.html',{'Movie':Movie})
def add(request):
    if request.method=="POST":
        name=request.POST.get('Name')
        desc = request.POST.get('Desc')
        year = request.POST.get('Year')
        img = request.FILES['img']
        Movie=movie(Name=name,Desc=desc,Year=year,img=img)
        Movie.save()
        return redirect('/')

    return render(request,'add.html')
def update(request,id):
    Movie=movie.objects.get(id=id)
    form=movieform(request.POST or None, request.FILES,instance=Movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'Movie':Movie})

def delete(request,id):
    if request.method=='POST':
        Movie=movie.objects.get(id=id)
        Movie.delete()
        return redirect('/')
    return render(request,'delete.html')
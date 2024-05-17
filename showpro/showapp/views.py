from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def moviedetails(request):
    return render(request,'moviedetail.html')
def addmovie(request):
    return render(request,'addmovie.html') 
def createuser(request):
    return render(request,'createuser.html')        
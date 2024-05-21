from django.shortcuts import render,redirect
from . models import moviedetails,bmsuser
from django.contrib.auth import authenticate,login
from django.contrib import messages

# Create your views here.
def index(request):
    movieobj=moviedetails.objects.all()
    return render(request,'index.html',{'movies':movieobj})
def moviedetailsdisplay(request):
    movieobj=moviedetails.objects.all()
    return render(request,'moviedetail.html',{'movies':movieobj})
    
    return render(request,'moviedetail.html')
def addmovie(request):
    if request.POST:
        moviename=request.POST.get('moviename')
        rating=request.POST.get('rating')
        appearence=request.POST.get('appearence')
        language=request.POST.get('language')
        duration=request.POST.get('duration')
        genre=request.POST.get('genre')
        certification=request.POST.get('cerification')
        releasedate=request.POST.get('releasedate')
        poster=request.POST.get('poster')
        banner=request.POST.get('banner')
        movieobj=moviedetails(moviename=moviename,rating=rating,appearence=appearence,language=language,duration=duration,genre=genre,certification=certification,releasedate=releasedate,poster=poster,banner=banner)
        movieobj.save()
        return redirect(addmovie)
    else:
        return render(request,'index.html',{'movies':movieobj})
def createuser(request):
    if request.POST:
        email=request.POST.get('email')
        age=request.POST.get('age')
        password=request.POST.get('password')
        userobj=bmsuser(email=email,age=age,password=password)
        userobj.save()
        return redirect(createuser)
    else :
        return render(request,'createuser.html')
def userauth(request):
    if request.POST:
        email=request.POST.get('email')
        password=request.POST.get('password')
        user = bmsuser.objects.filter(email=email).first()
        if user is not None:
            authen = authenticate(email=email, password=password)
            if authen is not None:
                  login(request, authen)
                  return render(request,'index.html')
            else:
                messages.error(request, 'Invalid email or password.')
                return render(request,'userauth.html')
        else:
            messages.error(request, 'User does not exist.')
            return render(request,'userauth.html')
    return render(request, 'userauth.html')

    
          
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('movie/',views.moviedetails,name='moviedetail'),
    path('addmovie/',views.addmovie,name='addmovie'),
    path('createuser/',views.createuser,name='createuser')
    ]
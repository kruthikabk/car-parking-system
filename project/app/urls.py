from django.contrib import admin
from django.urls import path , include
from app import views

urlpatterns = [
    path('' , views.index , name='index'),
    path('feedback' , views.feedback , name='feedback'),
    path('signup' , views.handlesignup , name='handlesignup'),
    path('login' , views.handlelogin , name='handlelogin'),
    path('handlelogout' , views.handlelogout , name='handlelogout'),
    path('reviews' , views.reviews , name='reviews'),
    path('search',views.search,name='search'),
    path('book' , views.book , name='book'),
    path('index2' , views.index2 , name='index2'),
    path('reservation' , views.reservation , name='reservation'),
    path('rules' , views.rules , name='rules'),
    path('about' , views.about , name='about'),
]
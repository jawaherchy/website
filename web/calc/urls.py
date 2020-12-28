from django.urls import path
from django.contrib import admin
from . import views
#for login
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path("",views.index, name='index'),
    path("services",views.services, name='services'),
    path("contact",views.contact, name='contact'),
    path("about",views.about, name='about'),
    #for login
    path('login',views.loginUser, name="login"),
    path('logout',views.logoutUser, name="logout"),
    path('travello',views.travello, name="travello"),

]
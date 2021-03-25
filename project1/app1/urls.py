"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import authenticateuser,signupuser,placeorder,userorders,adminorders,acceptorder,declineorder
from .views import adminloginview,adminhomepageview,authenticateadmin,logoutadmin,addfood,deletefood,homepageview,userloginview,customerhomepageview,userlogout



urlpatterns = [
    path('adminlogin/',adminloginview, name = 'adminloginpage'),
    path('adminauthenticate/',authenticateadmin),
    path('adminlogin/hompage/',adminhomepageview, name = 'adminhomepage'),
    path('adminlogout/',logoutadmin, name="logoutadmin"),
    path('addfood/',addfood),
    path('deletefood/<int:foodpk>/',deletefood),
    path('',homepageview, name="homepage"),
    path('signupuser/',signupuser),
    path('userlogin/',userloginview, name="userloginpage"),
    path('userauthenticate/',authenticateuser),
    path('customerhomepage/', customerhomepageview,name="customerhomepage"),
    path('userlogout/',userlogout,name="userlogout"),
    path('placeorder/',placeorder),
    path('userorders/',userorders),
    path('adminorders/',adminorders),
    path('acceptorder/<int:orderpk>/',acceptorder),
    path('declineorder/<int:orderpk>/',declineorder),
]
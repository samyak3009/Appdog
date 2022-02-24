from django.contrib import admin
from django.urls import path
from login import views
urlpatterns = [
    path('registeruser', views.RegisterUser.as_view()),
    path('loginuser', views.LoginUser.as_view()),
    path('userprofile/<pk>', views.UserProfile.as_view())
]
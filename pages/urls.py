from http.client import HTTPResponse
from django.contrib import admin
from django.urls import path
#from django.http import HTTPResponse
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutus/', views.aboutUs, name='aboutUs'),
    path('learn/', views.learn, name='learn'),
    path('home/', views.home, name='home'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('signup/', views.signup, name='signup'),
    path('feeds/', views.feeds, name='feeds'),
    path('create-post/', views.createRoom, name='create-post'),
    path('post/<str:pk>/', views.room, name='room'),

    path('update-user/', views.updateUser, name="update-user"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    path('update-post/<str:pk>/', views.updateRoom, name='update-room'),
    path('delete-post/<str:pk>/', views.deleteRoom, name='delete-room'),
    path('delete-message/<str:pk>/', views.deleteMessage, name='delete-message'),
    #path('lobby', views.lobby, name='lobby'),
    path('chat', views.chat, name='chat'),
    path('report', views.report, name='report'),






]
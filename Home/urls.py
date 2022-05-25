from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('academics', views.academics, name='academics'),
    path('placement', views.placement, name='placement'),
    path('contact', views.contact, name='contact'),
    path('forms/formPYQ', views.formPYQ, name='formPYQ'),
    path('forms/Calender', views.calender, name='Calender'),
    path('forms/timetable', views.timetable, name='timetable'),
    path('forms/assignmentForm', views.assignmentForm, name='assignmentForm'),
    path('forms/bookform', views.bookform, name='bookform'),
]
from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('index', views.index, name='home'),
    path('about', views.about, name='about'),
    path('academics', views.academics, name='academics'),
    path('placement', views.placement, name='placement'),
    path('contacts', views.contacts, name='contacts'),
    path('forms/formPYQ', views.formPYQ, name='formPYQ'),
    path('forms/Calender', views.calender, name='Calender'),
    path('forms/timetable', views.timetable, name='timetable'),
    path('forms/assignmentForm', views.assignmentForm, name='assignmentForm'),
    path('forms/bookform', views.bookform, name='bookform'),
    path('placements/dsa', views.dsa, name='dsa'),
    path('placements/cp', views.cp, name='cp'),
    path('placements/coresubject', views.coresubject, name='coresubject'),
    path('placements/project', views.project, name='project'),
    path('placements/resume', views.resume, name='resume'),
]
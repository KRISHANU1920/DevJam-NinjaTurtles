from django.shortcuts import render, HttpResponse
from django.template import loader
from .models import PYQ, Calender, Book, TimeTable, Assignment

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def academics(request):
    return render(request, 'academics.html')

def placement(request):
    return render(request, 'placement.html')

def contact(request):
    return render(request, 'contact.html')

def formPYQ(request):
    if request.method == 'POST':
        course = request.POST['course']
        branch = request.POST['branch']
        semester = request.POST['semester']
        exam = request.POST['exam']
        subject = request.POST['subject']
        myPYQ = PYQ.objects.filter(course=course, branch=branch, semester=semester, exam=exam, subject=subject)
        context = {
            'myPYQ': myPYQ,
        }
    
    else:
        context ={}
    template = loader.get_template('forms/formPYQ.html')
    return HttpResponse(template.render(context, request))

def calender(request):
    if request.method == 'POST':
        course = request.POST['course']
        branch = request.POST['branch']
        semester = request.POST['semester']
        myCal = Calender.objects.filter(course=course, branch=branch, semester=semester)
        context = {
            'myCal': myCal,
        }
    
    else:
        context ={}
    template = loader.get_template('forms/Calender.html')
    return HttpResponse(template.render(context, request))

def assignmentForm(request):
    if request.method == 'POST':
        course = request.POST['course']
        branch = request.POST['branch']
        Semester = request.POST['Semester']
        subject = request.POST['subject']
        myAsg = Assignment.objects.filter(course=course, branch=branch, Semester=Semester, subject=subject)
        context = {
            'myAsg': myAsg,
        }
    
    else:
        context ={}
    template = loader.get_template('forms/assignmentForm.html')
    return HttpResponse(template.render(context, request))

def timetable(request):
    if request.method == 'POST':
        course = request.POST['course']
        branch = request.POST['branch']
        semester = request.POST['semester']
        myTT = TimeTable.objects.filter(course=course, branch=branch, semester=semester)
        context = {
            'myTT': myTT,
        }
    
    else:
        context ={}
    template = loader.get_template('forms/timetable.html')
    return HttpResponse(template.render(context, request))

def bookform(request):
    if request.method == 'POST':
        Dept = request.POST['Dept']
        subject = request.POST['subject']
        myBook = Book.objects.filter(Dept=Dept, subject=subject)
        context = {
            'myBook': myBook,
        }
    
    else:
        context ={}
    template = loader.get_template('forms/bookform.html')
    return HttpResponse(template.render(context, request))
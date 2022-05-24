from django.shortcuts import render, HttpResponse
from django.template import loader
from .models import PYQ

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
from django.shortcuts import render, HttpResponse

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
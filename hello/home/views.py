from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from home.models import Services

# Create your views here.

def index(request):
    #python dictionary
   
    # return HttpResponse("This is my Homepage")
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    if request.method=="POST":
        flavour = request.POST.get('flavour')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        service = Services(flavour=flavour, email=email, phone=phone, message=message, date=datetime.today())
        service.save()

    return render(request, 'services.html')

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, phone=phone, message=message, date=datetime.today())
        contact.save()
    return render(request, 'contact.html')
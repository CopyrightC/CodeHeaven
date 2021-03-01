from django.shortcuts import render,HttpResponse
from datetime import datetime
from Home.models import Contact
from django.contrib import messages
def index(request):
    return render(request,'main.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        mail = request.POST.get('email')
        feedback = request.POST.get('feedback')
        cont = Contact(name=name,mail=mail,feedback=feedback,date=datetime.today())
        cont.save()
        messages.success(request,"Your feedback has been successfully sent!")
    return render(request,'contact.html')
def Escape(request):
    return render(request,'escape.html')

def Hacking(request):
    return render(request,'hacking.html')

def Pychat(request):
    return render(request,'pychat.html')


from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView

from django.core.mail import send_mail

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "sbs.html")
    
def about(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "about.html")
    
def facilities(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "facilities.html")
    
def gallery(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "gallery.html")    
    
def contact(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "contact.html")  
    
def robot(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "robot.txt")  
    
def sitemap(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "sitemap.xml")      



def send_gmail(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('subject')
        message = request.POST.get('message')

       
        email_message = f'{email} : {message}'
        
    

        send_mail(
            name,
            email_message,
            email,
            ['adhyapna@gmail.com'],
            fail_silently=False,
        )

        return HttpResponseRedirect(reverse('home'))
    else:
        return HttpResponse('Invalid request')

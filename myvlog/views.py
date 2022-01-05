from django.shortcuts import render
from .models import post

# Create your views here.
def home(request):
    all_post=post.objects.all()
    context={"all_post":all_post}
    return render(request,"myvlog/home.html",context)

def contact(request):
    return render(request,"myvlog/contact.html")

def about(request):
    return render(request,"myvlog/about.html")

def service(request):
    return render(request,"myvlog/service.html")    


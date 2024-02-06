from django.shortcuts import render
from shop.models import Category,Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
# Create your views here.
def allcategories(request):
    c=Category.objects.all()
    return render(request,'category.html',{'c':c})
def product(request,p):
    c=Category.objects.get(name=p)
    p=Product.objects.filter(category=c)
    return render(request, 'product.html',{'c':c,'p':p})
def details(request,p):
    p=Product.objects.get(name=p)
    return render(request,'details.html',{'p':p})
def register(request):
    return render(request,'register.html')

def register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        c=request.POST['c']
        e=request.POST['e']
        f=request.POST['f']
        l=request.POST['l']

        if (p==c):
            r=User.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l)
            r.save()
            return render (request,'category.html')

        else:
            return HttpResponse("Passwords are not same")

    return render(request,'register.html')
def user_login(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        l=authenticate(username=u,password=p)
        if l:
            login(request,l)
            return render (request,'category.html')
        else:
            return HttpResponse("Invalid credentials")
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return render(request,'login.html')
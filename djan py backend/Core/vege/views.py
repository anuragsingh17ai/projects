from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import  User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def recipes(request):
    if request.method=='POST':

        data=request.POST
        recipe_name=data.get('recipe_name')
        recipe_description=data.get('recipe_description')
        recipe_image=request.FILES.get('recipe_image')

        Reciepe.objects.create(
            recipe_name=recipe_name,
            recipe_description=recipe_description,
            recipe_image=recipe_image
            )
        return redirect('recipes')
    queryset=Reciepe.objects.all()
    if request.GET.get('search'):
        queryset=queryset.filter(recipe_name__icontains = request.GET.get('search'))
    return render(request,'receipes.html',context={'recipes':queryset})

def delete(request,id):
    queryset=Reciepe.objects.get(id=id)
    queryset.delete()
    return redirect('recipes')

def update(request,id):
    queryset=Reciepe.objects.get(id=id)

    if request.method=="POST":
        data=request.POST
        recipe_name=data.get('updaterecipe_name')
        recipe_description=data.get('updaterecipe_description')
        recipe_image=request.FILES.get('updaterecipe_image')

        queryset.recipe_name=recipe_name
        queryset.recipe_description=recipe_description

        if recipe_image:
            queryset.recipe_image=recipe_image
        queryset.save()
        return redirect('recipes')
    return render(request,'update.html',context={'query':queryset} )

def login_page(request):
    if request.method=='POST':
        data=request.POST
        username=data.get('username')
        password=data.get('password')

        queryset=User.objects.filter(username=username)
        if not queryset.exists():
            messages.error(request,"Invalid username")
            return redirect('login')
        # print(queryset.get(password=password))
        user=authenticate(username=username,password=password)
        
        if user is None:
            messages.info(request,"wrong Password")
        else:
            login(request,user)
            return redirect(request,'recipes')    
    return render(request,'login.html')

def logout_page(request):
    logout(request)
    return render('login')

def register(request):
    if request.method=='POST':
        data=request.POST
        first_name=data.get('first_name')
        last_name=data.get('last_name')
        username=data.get('username')
        password=data.get('password')

        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request, "User name Already taken.")
            return redirect('register')
        
        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        user.set_password(password)
        user.save()
        messages.info(request, "Registered succesfully.")
        return redirect('register')
    return render(request,'register.html')
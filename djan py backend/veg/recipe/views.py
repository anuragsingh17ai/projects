from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
# Create your views here.
def home(request):
    # return HttpResponse('hi')
    if request.method=='POST':
        data=request.POST
        recipe_name=data.get('recipe_name')
        recipe_desc=data.get('recipe_desc')
        recipe_img=request.FILES.get('recipe_img')

        Data.objects.create(
            recipe_name=recipe_name,
            recipe_desc=recipe_desc,
            recipe_img=recipe_img
        )
        
        return redirect('/')
    query_set=Data.objects.all()
    return render(request,'index.html',context={'recipe':query_set})


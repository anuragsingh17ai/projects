from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("hey i am here")

def success_page(request):
    return HttpResponse("<h1>This is success page </h1>")
def page(request):
    people=[
        {'name':'Anurag','age':23},
        {'name':'Adarsh','age':22}
    ]
    return render(request,'index.html',context={'pep':people})
    
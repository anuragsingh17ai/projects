from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('student',post_student,name='post_student')
]
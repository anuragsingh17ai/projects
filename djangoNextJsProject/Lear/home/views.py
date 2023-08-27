from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
@api_view(['GET'])
def home(request):
    student_objs=Student.objects.all()
    serializer=StudentSerializer(student_objs,many=True)
    return Response({'Status':200,'message':serializer.data})

@api_view(['POST'])
def post_student(request):
    data=request.data
    print(data)
    return Response({'status':200,'message':'you sent'})

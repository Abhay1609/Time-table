from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework import permissions
from rest_framework.permissions  import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi 
from rest_framework.generics import ListCreateAPIView
from django.conf import settings
from django.utils.translation import gettext_lazy 
import json 
from django.views.decorators.csrf import csrf_exempt
from .serializers import *
from .models import Lecture
from account.models import User
import io
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
# Create your views here.
@csrf_exempt
def lecture_create(request):

    if request.method == 'POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer=LectureSerializers(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data Created'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
def lecture_view(request,pk,pki,pkyear):
    if request.method == 'GET':


        stu=Lecture.objects.filter(year=pkyear).filter(branche=pk).filter(section=pki)
        serializer = LectureSerializers(stu,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
def teacher_view(request,teacher):
    if request.method == 'GET':


        stu=Lecture.objects.filter(faculty=teacher)
        serializer = LectureSerializers(stu,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
class Time_Table_Data(ListCreateAPIView):
    serializer_class=TimeTableSerializer
    queryset=Lecture.objects.filter(day=1)
    def get_queryset(self):
        class_id=self.kwargs.get('class_id')
        return self.queryset.filter(cid=class_id)
@api_view(['GET'])
def TimeTableData(request,class_id):
    data=Lecture.objects.filter(cid=class_id)
    Monday=[]
    Tuesday=[]
    Wednesday=[]
    Thursday=[]
    Friday=[]
    for day in data:
        if day.day=="1":
            Monday.append(day)
        elif day.day=="2":
            Tuesday.append(day)
        elif day.day=="3":
            Wednesday.append(day)
        elif day.day=="4":
            Thursday.append(day)
        elif day.day=="5":
            Friday.append(day)
    serializer1=TimeTableSerializer(Monday,many=True)
    serializer2=TimeTableSerializer(Tuesday,many=True)
    serializer3=TimeTableSerializer(Wednesday,many=True)
    serializer4=TimeTableSerializer(Thursday,many=True)
    serializer5=TimeTableSerializer(Friday,many=True)
    serializer=TimeTableSerializer(data,many=True)
    return Response({"Monday":serializer1.data,"Tuesday":serializer2.data,"Wednesday":serializer3.data,"Thursday":serializer4.data,"Friday":serializer5.data},status=status.HTTP_200_OK)



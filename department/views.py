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
from .models import *
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
@api_view(['GET'])
def teacher_view(request,teacher):
    stu=Lecture.objects.filter(faculty=teacher)
    Monday = []
    Tuesday = []
    Wednesday = []
    Thursday = []
    Friday = []
    Saturday=[]
    free= Lecture.objects.get(id="310")
    for day in stu:
        if day.day == "1":
            Monday.append(day)
        elif day.day == "2":
            Tuesday.append(day)
        elif day.day == "3":
            Wednesday.append(day)
        elif day.day == "4":
            Thursday.append(day)
        elif day.day == "5":
            Friday.append(day)
        elif day.day == "6":
            Saturday.append(day)
    all=[Monday,Tuesday,Wednesday,Thursday,Friday,Saturday]
    less_day=[]
    days_now=[]
    arr=[1,2,4,5,6,7,8,9]
    i=0
    for day in all:
        i=i+1
        if len(day)<8:
            less_day.append(day)
            days_now.append(i)
    thatday=[]
    less_day=zip(less_day,days_now)
    for days,day_now in less_day:
        if len(days)==0:
            thatday=[]
            for i in range(8):
                free= Lecture.objects.get(id="310")
                if i<2:
                    period=Period.objects.get(id=i+1)
                if i>=2:
                    period=Period.objects.get(id=i+2)
                free.period=period
                free.day=day_now
                thatday.append(free)
        else:
            class_period=[]
            thatday=[]
            for datas in days:
                class_period.append(datas.period.period_no)
            diff=list(set(arr)-set(class_period))
            l=0
            for i in range(0,8):
                if i<2:
                    m=i+1
                if i>=2:
                    m=i+2
                if m in diff:
                    free= Lecture.objects.get(id="310")
                    period=Period.objects.get(id=m)
                    free.period=period
                    free.day=day_now
                    thatday.append(free)
                if m not in diff:
                    thatday.append(days[l])
                    l+=1
        # period=Period.objects.get(id="1")
        # free.period=period
        #Instead of the data ,address was append in the that day if I will change the value of free here then it will be reflected in output.
        if day_now==1:
            Monday=thatday
        elif day_now==2:
            Tuesday=thatday
        elif day_now==3:
            Wednesday=thatday
        elif day_now==4:
            Thursday=thatday
        elif day_now==5:
            Friday=thatday
        elif day_now==6:
            Saturday=thatday 
    serializer1=TimeTableSerializer(Monday,many=True)
    serializer2=TimeTableSerializer(Tuesday,many=True)
    serializer3=TimeTableSerializer(Wednesday,many=True)
    serializer4=TimeTableSerializer(Thursday,many=True)
    serializer5=TimeTableSerializer(Friday,many=True)
    serializer6=TimeTableSerializer(Saturday,many=True)
    return Response({"Monday":serializer1.data,"Tuesday":serializer2.data,"Wednesday":serializer3.data,"Thursday":serializer4.data,"Friday":serializer5.data,"Saturday":serializer6.data},status=status.HTTP_200_OK)
@api_view(['GET'])
def Time_Table_day(request,day,class_id):
    if request.method == 'GET':
        stu = Lecture.objects.filter(cid=class_id).filter(day=day)
        serializer = TimeTableSerializer(stu,many=True)
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
    lunch=Class.objects.get(id=class_id)
    lunch=lunch.lunch.period_no
    Monday=[]
    Tuesday=[]
    Wednesday=[]
    Thursday=[]
    Friday=[]
    Saturday=[]
    free= Lecture.objects.get(id="310")
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
        elif day.day == "6":
            Saturday.append(day)
    all=[Monday,Tuesday,Wednesday,Thursday,Friday,Saturday]
    less_day=[]
    days_now=[]
    arr=[1,2,4,5,6,7,8,9]
    arr.remove(lunch)
    i=0
    for day in all:
        i=i+1
        if len(day)<7:
            less_day.append(day)
            days_now.append(i)
    thatday=[]
    less_day=zip(less_day,days_now)
    for days,day_now in less_day:
        if len(days)==0:
            thatday=[]
            for i in range(7):
                free= Lecture.objects.get(id="310")
                if i<2:
                    period=Period.objects.get(id=i+1)
                if i>=2 and i<lunch-2:
                    period=Period.objects.get(id=i+2)
                if i>=lunch-2:
                    period=Period.objects.get(id=i+3)
                free.period=period
                free.day=day_now
                thatday.append(free)
        else:
            class_period=[]
            thatday=[]
            for datas in days:
                class_period.append(datas.period.period_no)
            diff=list(set(arr)-set(class_period))
            l=0
            for i in range(0,7):
                if i<2:
                    m=i+1
                if i>=2 and i<lunch-2:
                    m=i+2
                if i>=lunch-2:
                    m=i+3
                if m in diff:
                    free= Lecture.objects.get(id="310")
                    period=Period.objects.get(id=m)
                    free.period=period
                    free.day=day_now
                    thatday.append(free)
                if m not in diff:
                    thatday.append(days[l])
                    l+=1
        if day_now==1:
            Monday=thatday
        elif day_now==2:
            Tuesday=thatday
        elif day_now==3:
            Wednesday=thatday
        elif day_now==4:
            Thursday=thatday
        elif day_now==5:
            Friday=thatday
        elif day_now==6:
            Saturday=thatday
        
    serializer1=TimeTableSerializer(Monday,many=True)
    serializer2=TimeTableSerializer(Tuesday,many=True)
    serializer3=TimeTableSerializer(Wednesday,many=True)
    serializer4=TimeTableSerializer(Thursday,many=True)
    serializer5=TimeTableSerializer(Friday,many=True)
    serializer6=TimeTableSerializer(Saturday,many=True)
    return Response({"Monday":serializer1.data,"Tuesday":serializer2.data,"Wednesday":serializer3.data,"Thursday":serializer4.data,"Friday":serializer5.data,"Saturday":serializer6.data},status=status.HTTP_200_OK)

@api_view(['GET'])
def period_view(request):

    if request.method == 'GET':

        stu = Period.objects.all()
        serializer = PeriodSerializers(stu, many=True)

        return Response(serializer.data)
@api_view(['POST'])
def CreateTable(request):
    serializer=TimeTableCreateSerializer(data=request.data)
    subject=request.data["subject_id"]
    day=1
    period=1
    counter=0
    limit=request.data["no_of_lectures"]
    type=request.data["type"]
    faculty=request.data["teacher_id"]
    print(subject)
    if type=="THEORY":
        for section in request.data["class_id"]:
            for i in range(1,limit+1):
                lecture={
                    "period":period,
                    "cid":section,
                    "day":day,
                    "faculty":faculty,
                    "subject":subject,
                    "type":type,
                }
                data=LectureCreateSerializer(data=lecture)
                if data.is_valid():
                    data.save()
                while data.is_valid()==False:
                    counter+=1
                    print(counter)
                    if counter==36:
                        return Response({"Message":"No Slot available"})
                    period+=1
                    if period==3 or period==7:
                        period+=1
                    if period>9:
                        day+=1
                        period=1
                    if day>5:
                        day=1
                    lecture={
                    "period":period,
                    "cid":section,
                    "day":day,
                    "faculty":faculty,
                    "subject":subject,
                    "type":type,
                        }
                    data=LectureCreateSerializer(data=lecture)
                    if data.is_valid():
                        data.save()
                day=day+1
                period=period+1
                if day>5:
                    day=1
                if period==3 or period==7:
                    period+=1
                if period>9:
                    period=1
                    day+=1
                if day>5:
                    day=1
        return Response({"Message":"Data for Theory Classes has been generated"})
    elif type=="LAB":
        for section in request.data["class_id"]:
            for i in range(1,limit+1):
                if day>5:
                    day=1
                if period==2 or period==6:
                    period+=1
                if period==3 or period==7:
                    period+=1
                if period>8:
                    day+=1
                    period=1
                if day>5:
                    day=1
                lecture={
                    "period":period,
                    "cid":section,
                    "day":day,
                    "faculty":faculty,
                    "subject":subject,
                    "type":type,
                    }
                lecture1={
                    "period":period+1,
                    "cid":section,
                    "day":day,
                    "faculty":faculty,
                    "subject":subject,
                    "type":type,
                    }

                data=LectureCreateSerializer(data=lecture)
                data1=LectureCreateSerializer(data=lecture1)
                if data.is_valid() and data1.is_valid():
                    data.save()
                    data1.save()
                while data.is_valid()==False or data1.is_valid()==False:
                    counter+=1
                    if counter==36:
                        return Response({"Message":"No Slot available"})
                    period+=1
                    if period==2 or period==6:
                        period+=1
                    if period==3 or period==7:
                        period+=1
                    if period>8:
                        day+=1
                        period=1
                    if day>5:
                        day=1
                    lecture={
                    "period":period,
                    "cid":section,
                    "day":day,
                    "faculty":faculty,
                    "subject":subject,
                    "type":type,
                        }
                    lecture1={
                    "period":period+1,
                    "cid":section,
                    "day":day,
                    "faculty":faculty,
                    "subject":subject,
                    "type":type,
                    }
                    data=LectureCreateSerializer(data=lecture)
                    data1=LectureCreateSerializer(data=lecture1)
                    if data.is_valid() and data1.is_valid():
                        data.save()
                        data1.save()
                day=day+1
                period=period+1
                if day>5:
                    day=1
                if period==2 or period==6:
                    period+=1
                if period==3 or period==7:
                    period+=1
                if period>8:
                    period=1
                    day+=1
                if day>5:
                    day=1
        return Response({"Message":"Data for lab classes has been created"})





from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .serializers import LectureSerializers
from .models import Lecture
import io
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
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


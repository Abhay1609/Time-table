from rest_framework import serializers
from .models import *
class LectureSerializers(serializers.Serializer):
    day = serializers.CharField(max_length=100)
    time=serializers.CharField(max_length=100)
    faculty=serializers.CharField(max_length=100)
    subject = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Lecture.objects.create(**validated_data)
class TimeTableSerializer(serializers.ModelSerializer):
    cid= serializers.CharField(source='cid.class_id')
    faculty=serializers.CharField(source='faculty.full_name')
    subject=serializers.CharField(source='subject.subject')
    period=serializers.CharField(source='period.timeslot')
    class Meta:
        model=Lecture
        fields="__all__"
class PeriodSerializers(serializers.Serializer):
    period_no=serializers.IntegerField()
    timeslot=serializers.CharField(max_length=11)
class TimeTableCreateSerializer(serializers.Serializer):
    teacher_id=serializers.CharField(max_length=5)
    subject_id=serializers.CharField(max_length=5)
    class_id=serializers.ListField(child=serializers.CharField(max_length=5))
    no_of_lectures=serializers.IntegerField()
class LectureCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Lecture
        fields="__all__"
    
   
        

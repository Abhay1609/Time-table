from rest_framework import serializers
from .models import Lecture
class LectureSerializers(serializers.Serializer):
    day = serializers.CharField(max_length=100)
    time=serializers.CharField(max_length=100)
    faculty=serializers.CharField(max_length=100)
    subject = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Lecture.objects.create(**validated_data)
class TimeTableSerializer(serializers.ModelSerializer):
    cid= serializers.CharField(source='cid.branch')
    faculty=serializers.CharField(source='faculty.full_name')
    subject=serializers.CharField(source='subject.subject')
    period=serializers.CharField(source='period.timeslot')
    class Meta:
        model=Lecture
        fields="__all__"

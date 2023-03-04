from rest_framework import serializers
from .models import Lecture
class LectureSerializers(serializers.Serializer):
    branche = serializers.CharField(max_length=100)
    section = serializers.IntegerField()
    year=serializers.IntegerField()


    day = serializers.CharField(max_length=100)
    time=serializers.CharField(max_length=100)
    faculty=serializers.CharField(max_length=100)
    subject = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Lecture.objects.create(**validated_data)

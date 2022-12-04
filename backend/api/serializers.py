from .models import *
from rest_framework import serializers

class WorkerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 55)
    desc = serializers.CharField()
    stype = serializers.ChoiceField(choices=stuff_type, default=stuff_type[0])
    img = serializers.ImageField(use_url="workers/", default="")

class SectionSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response

class GetWorkers(APIView):
    def get(self, request):
        key = None
        if 'type' in request.GET:
            key = request.GET['type']
        
        if key:
            queryset = Worker.objects.all().filter(stype=key)
        else:
            queryset = Worker.objects.all()
        serialized = WorkerSerializer(instance=queryset, many=True)
        return Response(serialized.data)

class GetSections(APIView):
    def get(self, request):
        queryset = Section.objects.all().exclude(id=1)
        serialized = SectionSerializer(instance=queryset, many=True)
        return Response(serialized.data)
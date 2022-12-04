from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('get_workers', GetWorkers.as_view()),
    path('get_sections', GetSections.as_view()),
]
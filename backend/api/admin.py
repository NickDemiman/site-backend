from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    search_fields = ('name',)

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    search_fields = ('name',)
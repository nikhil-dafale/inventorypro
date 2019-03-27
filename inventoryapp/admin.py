from django.contrib import admin
from .models import Components,Metals,Plastics,Composites
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class ComponentAdmin(admin.ModelAdmin):
    list_display =['type','price','status','issues']



@admin.register(Metals,Plastics,Composites)
class ViewAdmin(ImportExportModelAdmin):
    pass
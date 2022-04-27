from django.contrib import admin
from . models import Plate
# Register your models here.
@admin.register(Plate)
class StudentAdmin(admin.ModelAdmin):
    list_display=('idplate','plateNo','phoneNo')

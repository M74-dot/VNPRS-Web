from django.contrib import admin
from . models import Student
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('id','student_name','college_name','Specialisation','degree','internship','phoneNo','email','location','gender','notes')

from django.contrib import admin
from App.models import Student

@admin.register(Student)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "age"]
from django.contrib import admin
from homework.models import Student
from homework.models import Score, Subject

admin.site.register(Student)
admin.site.register(Score)
admin.site.register(Subject)

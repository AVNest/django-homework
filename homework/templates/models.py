from django.db import models

class Student(models.Model):
    name = models.CharFiled(max_length=32, null=False)
    surname = models.CharFiled(max_length=32, null=False)


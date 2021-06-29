from django.db import models
import datetime


class Habit(models.Model):
    name = models.CharField(max_length=100)
    start_day=models.DateTimeField(auto_now_add=False, default=datetime.datetime.today())
    do_it=models.BooleanField(null=True)
    do_it_list=models.TextField(null=True)
    end=models.BooleanField(null=False, default=False)

    def __str__(self):
        return self.name

class end_Habit(models.Model):
    name = models.CharField(max_length=100)
    start_day=models.DateTimeField(auto_now_add=False, default=datetime.datetime.today())
    do_it_list=models.TextField(null=True)

    def __str__(self):
        return self.name

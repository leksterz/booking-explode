from django.db import models

# Create your models here.
class Request(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def __str__(self):
        return f'Request id: {self.id}, name: {self.name}, date: {self.date}, start time: {self.start_time}, end time: {self.end_time}, status: {self.status}'

class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=20)

    class Meta:
        ordering = ['start_time']

    def __str__(self):
        return f'Schedule id: {self.id}, date: {self.date}, start time: {self.start_time}, end time: {self.end_time}, status: {self.status}'

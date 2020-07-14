from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Schedule(models.Model):
    bookScheduleTeam = models.CharField(max_length=100, blank=False)
    bookScheduleStartDate = models.DateTimeField(default=timezone.now)
    bookScheduleEndDate = models.DateTimeField(default=timezone.now)
    bookScheduleDescription = models.TextField()

    def __str__(self):
        return self.bookScheduleTeam

    def get_absolute_url(self): # redirect 활용 시
        return reverse('schedule_detail', args=[self.id])
        
    

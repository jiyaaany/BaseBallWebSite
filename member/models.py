from django.db import models
from django.utils import timezone

# Create your models here.

class Ticket(models.Model):
    username = models.CharField(max_length=50, null=True)
    ticket_type = models.CharField(max_length=100)
    is_show = models.BooleanField(default=True)
    is_del = models.BooleanField(default=False)
    ticket_cnt = models.IntegerField(default=0)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    reg_date = models.DateTimeField(default=timezone.now)
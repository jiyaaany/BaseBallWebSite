from django.contrib import admin
from .models import Schedule

# Register your models here.
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'bookScheduleTeam', 'bookScheduleStartDate', 'bookScheduleEndDate', 'bookScheduleDescription')

admin.site.register(Schedule, ScheduleAdmin)
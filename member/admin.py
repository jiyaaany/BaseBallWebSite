from django.contrib import admin
from .models import Ticket

# Register your models here.

class TicketAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'ticket_type', 'is_del', 'start_date', 'end_date', 'reg_date')

admin.site.register(Ticket, TicketAdmin)
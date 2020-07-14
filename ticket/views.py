from django.shortcuts import render
from member.models import Ticket
import datetime
from dateutil.relativedelta import relativedelta

# Create your views here.
def accept_ticket(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    ticket.start_date = datetime.date.now()

    if ticket.ticket_type == 'month1' or ticket.ticket_type == 'coupon4' or ticket.ticket_type == 'coupon8':
        ticket.end_date = datetime.date.now() + relativedelta(months=1)
    elif ticket.ticket_type == 'month3':
        ticket.end_date = datetime.date.now() + relativedelta(months=3)
    elif ticket.ticket_type == 'month6':
        ticket.end_date = datetime.date.now() + relativedelta(months=6)
    elif ticket.ticket_type == 'coupon20':
        ticket.end_date = datetime.date.now() + relativedelta(months=4)
    
    tickets = Ticket.objects.all()
    context = {'tickets' : tickets}
    return render(request, 'ask_ticket.html', context)

def reject_ticket(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    ticket.is_del = True
    ticket.save()
    
    tickets = Ticket.objects.filter(is_del=False)
    context = {'tickets' : tickets}
    return render(request, 'ask_ticket.html', context)
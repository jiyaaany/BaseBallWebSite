from django.shortcuts import render, redirect
from accounts.models import User
from .models import Ticket

# Create your views here.
def manage_member(request):
    members = User.objects.order_by('username')
    context = {'members' : members}
    return render(request, 'manage_member.html', context)

def member_detail(request, username):
    member = User.objects.get(username=username)
    context = {'member' : member}
    return render(request, 'member_detail.html', context)

def buy_ticket(request):
    return render(request, 'buy_ticket.html')

def request_ticket(request):
    if request.method == "GET":
        ticket = Ticket.objects.create(
            username = request.user.username,
            ticket_type=request.GET['ticket']
        )
    return render(request, 'request_success.html')
    
def ask_ticket(request):
    tickets = Ticket.objects.filter(is_del=False, is_show=True)
    context = {'tickets' : tickets}
    return render(request, 'ask_ticket.html', context)




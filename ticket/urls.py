from django.urls import path
from . import views

app_name = 'ticket'
urlpatterns = [
    path('accept_ticket/<int:ticket_id>', views.accept_ticket, name="accept_ticket"),
    path('reject_ticket/<int:ticket_id>', views.reject_ticket, name="reject_ticket"),
]
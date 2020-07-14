from django.urls import path
from . import views

app_name = 'member'
urlpatterns = [
    path('manage_member/', views.manage_member, name='manage_member'),
    path('member_detail/<username>/', views.member_detail, name='member_detail'),
    path('buy_ticket', views.buy_ticket, name='buy_ticket'),
    path('request_ticket', views.request_ticket, name='request_ticket'),
    path('ask_ticket', views.ask_ticket, name="ask_ticket"),
]
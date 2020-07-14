from django.shortcuts import render, redirect
from .forms import ScheduleForm
from .models import Schedule

# Create your views here.
def book_schedule(request):
    return render(request, 'book_schedule.html')

def show_schedule(request):
    schedules = Schedule.objects.all()
    context = {'schedules' : schedules}
    return render(request, 'show_schedule.html', context)

def schedule_form(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schedule:show_schedule')
    else:
        form = ScheduleForm()
    return render(request, 'schedule_form.html', {'form' : form})

def create_schedule(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST, request.FILES) # parameters 순서 주의
        if form.is_valid():
            form = Form(bookScheduleTeam = form.cleaned_data['bookScheduleTeam'],
                        bookScheduleStartDate = form.cleaned_data['bookScheduleStartDate'],
                        bookScheduleEndDate = form.cleaned_data['bookScheduleEndDate'],
                        bookScheduleDescription = form.cleaned_data['bookScheduleDescription'])
            post.svae()
            return render(form)
    else:
        form = ScheduleForm()
        return render(request, 'book_schedule.html',{
            'form' : form,
        })
    return render(request, 'show_schedule.html', {'form' : form})

def schedule_detail(request, pk):
    schedule = Schedule.objects.get(pk=pk)
    context = {'schedule' : schedule}
    return render(request, 'schedule_detail.html', context)

def cancel_schedule(request, pk):
    schedule = Schedule.objects.get(pk=pk)
    schedule.delete()
    return redirect('schedule:show_schedule')
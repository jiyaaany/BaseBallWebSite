from django import forms
from django.utils import timezone
from .models import Schedule

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['bookScheduleTeam', 'bookScheduleStartDate', 'bookScheduleEndDate', 'bookScheduleDescription']

    def __init__(self, *args, **kwargs):
        super(ScheduleForm, self).__init__(*args, **kwargs)
        self.fields['bookScheduleTeam'].label = ""
        self.fields['bookScheduleStartDate'].label = ""
        self.fields['bookScheduleEndDate'].label = ""
        self.fields['bookScheduleDescription'].label = ""
        self.fields['bookScheduleTeam'].widget.attrs.update({
            'class' : 'form-control',
            'placeholder' : '대관 팀명을 입력하세요.'
        })
        self.fields['bookScheduleDescription'].widget.attrs.update({
            'class' : 'form-control',
            'placeholder' : '대관 목적을 입력하세요.'
        })
        

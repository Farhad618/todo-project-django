from django import forms
from .models import Tasks
from django.contrib.admin.widgets import AdminSplitDateTime
import datetime

TASK_PRIORITY_CHOICES = [
    ('0', 'Normal'),
    ('1', 'Important'),
    ('2', 'High'),
    # ('3', 'Black'),
    # ('4', 'Black'),
]

class TaskForm(forms.ModelForm):
	# due_date = forms.SplitDateTimeField(widget=AdminSplitDateTime())
	# due_date = forms.DateField()
	due_date = forms.DateField(
	        # input_formats=['%d/%m/%Y'],
	        widget=forms.DateInput(attrs={'type': 'date', 'min':datetime.datetime.now().date()})
	    )
	due_time = forms.TimeField(
	        widget=forms.TimeInput(attrs={'type': 'time', 'min':datetime.datetime.now().time().strftime('%H:%S')})
	    )
	tsk_priority = forms.ChoiceField(widget=forms.RadioSelect, choices=TASK_PRIORITY_CHOICES)
	class Meta:
		model = Tasks
		fields = '__all__'
		# widgets = {'due_date': forms.DateInput(format=('%d-%m-%Y'), 
                                             # attrs={'class':'myDateClass', 
                                            # 'placeholder':'Select a date'})}
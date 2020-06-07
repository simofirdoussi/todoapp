from django import forms
from django.forms import ModelForm

from .models import *


class TaskForm(forms.ModelForm):
	description= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...','class':'form-control'}))
	date = forms.DateTimeField(widget= forms.SelectDateWidget())
	
	class Meta:
		model = Task
		exclude = ["user"]
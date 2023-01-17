from django import forms
from .models import *


class Taskform(forms.ModelForm):

    class Meta:
        model = Task
        fields = "__all__"




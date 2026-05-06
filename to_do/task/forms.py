from django import forms
from .models import AddTasks, UpdateTask

class Add_task(forms.ModelForm):
    class Meta:
        model = AddTasks
        fields = [
            'title', 'status'
        ]

class Update_task(forms.ModelForm):
    class Meta:
        model = UpdateTask
        fields = ['tsk','status']

class List_tsk(forms.ModelForm):
    class Meta:
        model = AddTasks
        fields = ['title','status']


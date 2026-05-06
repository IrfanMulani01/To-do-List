from django.db import models

class AddTasks(models.Model):
    status_choice = [
        ('complate', 'Complate'),
        ('incomplate', 'Incomplate'),
        ('high', 'High Priority'),
    ]
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=status_choice, default='incomplate')


    def __str__(self):
        return self.title
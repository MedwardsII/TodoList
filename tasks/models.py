from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    task = models.CharField(
        max_length=200
    )
    is_complete = models.BooleanField(
        default=False,
        help_text='The completion status of the task.'
    )
    due_date = models.DateField(
        blank=True,
        null=True,
        help_text='Date task is scheduled to be completed.'
    )
    modified_date = models.DateTimeField(
        auto_now=True,
        help_text='Date task was last modified.'
    )
    created_date = models.DateTimeField(
        auto_now_add=True,
        help_text='Date task was created.'
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    def __str__(self):
        return str(self.pk)
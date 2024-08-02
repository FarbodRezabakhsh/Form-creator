from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Form(models.Model):
    FORM_TYPE_CHOICES = [
        ('survey', 'Survey'),
        ('quiz', 'Quiz'),
        ('poll', 'Poll'),
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    form_type = models.CharField(max_length=20, choices=FORM_TYPE_CHOICES)
    description = models.TextField()
    is_private = models.BooleanField(default=False)
    password = models.CharField(max_length=100, blank=True, null=True)
    view_counts = models.PositiveIntegerField(default=0)
    # answer_counts = models.PositiveIntegerField(default=0)
    user_answer_counts = models.PositiveIntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description[:10]

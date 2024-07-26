from django.db import models
from django.contrib.auth.models import User

class Form(models.Model):
    FORM_TYPE_CHOICES = [
        ('survey', 'Survey'),
        ('quiz', 'Quiz'),
        ('poll', 'Poll'),
    ]

    form_type = models.CharField(max_length=20, choices=FORM_TYPE_CHOICES)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    is_private = models.BooleanField(default=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    view_counts = models.PositiveIntegerField(default=0)
    answer_counts = models.PositiveIntegerField(default=0)
    user_answer_counts = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.description[:50]

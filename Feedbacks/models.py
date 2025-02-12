from django.contrib.auth.models import User
from Forms.models import Form
from django.db import models
# Create your models here.


class Question(models.Model):
    CHOICES = [
        ('survey','Survey'),
        ('quiz','Quiz'),
        ('poll','Poll')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='questions')
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    question_type = models.CharField(max_length=255,choices=CHOICES)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

    def get_question_by_form_type(form_type):
        return Question.objects.filter(form__form_type=form_type)


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE,related_name='answers')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Answer to {self.question.title} - {self.user.username}'

    def get_answers_by_question_type(form_type):
        return Answer.objects.filter(question__form__form_type=form_type)
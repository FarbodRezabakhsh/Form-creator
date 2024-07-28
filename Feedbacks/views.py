from django.shortcuts import render
from .models import Question,Answer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from .serializers import QuestionSerializer,AnswerSerializer

# Create your views here.

class QuestionViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    def get_queryset(self):
        form_type = self.request.query_params.get('form_type', None)
        if form_type:
            return Question.get_questions_by_type(form_type)
        return super().get_queryset()


class AnswerViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()

    def get_queryset(self):
        form_type = self.request.query_params.get('form_type', None)
        if form_type:
            return Answer.get_answers_by_question_type(form_type)
        return super().get_queryset()
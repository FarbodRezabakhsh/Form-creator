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


class AnswerViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
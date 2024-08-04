from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Question,Answer
from rest_framework import viewsets
from .serializers import QuestionSerializer,AnswerSerializer
from rest_framework import status
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle

# Create your views here.

class QuestionListView(APIView):
    throttle_classes = [AnonRateThrottle]
    def get(self,request):
        question = Question.objects.all()
        srz_data = QuestionSerializer(instance=question,many=True)
        return Response(data=srz_data.data,status=status.HTTP_200_OK)

class QuestionCreateView(APIView):
    def post(self,request):
        srz_data = QuestionSerializer(data=request.POST)
        if srz_data.is_valid():
            srz_data.save()
            return Response(data=srz_data.data,status=status.HTTP_201_CREATED)
        return Response(data=srz_data.errors,status=status.HTTP_400_BAD_REQUEST)

class QuestionUpdateView(APIView):
    def put(self,request,pk):
        question = Question.objects.get(pk=pk)
        srz_data = QuestionSerializer(instance=question,data=request.POST,partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data,status=status.HTTP_200_OK)
        return Response(srz_data.errors,status=status.HTTP_400_BAD_REQUEST)

class QuestionDeleteView(APIView):
    def delete(self,request,pk):
        question = Question.objects.get(pk=pk)
        question.delete()
        return Response({'message':'question deleted'})

class AnswerViewSet(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()

    def get_queryset(self):
        form_type = self.request.query_params.get('form_type', None)
        if form_type:
            return Answer.get_answers_by_question_type(form_type)
        return super().get_queryset()
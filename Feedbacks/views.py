from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Question,Answer
from rest_framework import viewsets
from .serializers import QuestionSerializer,AnswerSerializer
from rest_framework import status
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from permissions import IsOwnerOrReadOnly


# Create your views here.

class QuestionListView(APIView):
    """
        Listing all questions
    """
    throttle_classes = [AnonRateThrottle,UserRateThrottle]
    serializer_class = QuestionSerializer

    def get(self,request):
        question = Question.objects.all()
        srz_data = QuestionSerializer(instance=question,many=True)
        return Response(data=srz_data.data,status=status.HTTP_200_OK)

class QuestionCreateView(APIView):
    """
        Create a new question
    """
    serializer_class = QuestionSerializer
    def post(self,request):
        srz_data = QuestionSerializer(data=request.POST)
        if srz_data.is_valid():
            srz_data.save()
            return Response(data=srz_data.data,status=status.HTTP_201_CREATED)
        return Response(data=srz_data.errors,status=status.HTTP_400_BAD_REQUEST)

class QuestionUpdateView(APIView):
    """
        Update a question
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = QuestionSerializer
    def put(self,request,pk):
        question = Question.objects.get(pk=pk)
        self.check_object_permissions(request,question)
        srz_data = QuestionSerializer(instance=question,data=request.POST,partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data,status=status.HTTP_200_OK)
        return Response(srz_data.errors,status=status.HTTP_400_BAD_REQUEST)

class QuestionDeleteView(APIView):
    """
        Deleting a question
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = QuestionSerializer
    def delete(self,request,pk):
        question = Question.objects.get(pk=pk)
        question.delete()
        return Response({'message':'question deleted'})

class AnswerListView(APIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    serializer_class = AnswerSerializer

    def get(self,request):
        answers = Answer.objects.all()
        srz_data = AnswerSerializer(instance=answers,many=True)
        return Response(srz_data.data,status=status.HTTP_200_OK)

class AnswerCreateView(APIView):
    """
        Create a new answer
    """
    serializer_class = AnswerSerializer

    def post(self, request):
        srz_data = AnswerSerializer(data=request.POST)
        if srz_data.is_valid():
            srz_data.save()
            return Response(data=srz_data.data, status=status.HTTP_201_CREATED)
        return Response(data=srz_data.errors, status=status.HTTP_400_BAD_REQUEST)

class AnswerUpdateView(APIView):
    """
        Update a answer
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = AnswerSerializer
    def put(self,request,pk):
        answer = Answer.objects.get(pk=pk)
        srz_data = self.serializer_class(instance=answer,data=request.POST,partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data,status=status.HTTP_200_OK)
        return Response(srz_data.errors,status=status.HTTP_400_BAD_REQUEST)


class AnswerDeleteView(APIView):
    """
        Deleting an answer
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = AnswerSerializer

    def delete(self, request, pk):
        answer = Answer.objects.get(pk=pk)
        answer.delete()
        return Response({'message': 'Answer deleted'}, status=status.HTTP_204_NO_CONTENT)
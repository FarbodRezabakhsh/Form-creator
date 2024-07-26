from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from rest_framework import viewsets, status, generics
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Form
from .serializers import FormSerializer
from permissions import IsOwnerOrReadOnly
from .pagination import CustomPagination


'''class FormViewSet(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = FormSerializer

    def get(self, request):
        posts = Form.objects.all()  # You can adjust the queryset as needed
        serializer = self.serializer_class(posts, many=True, context={'request': request})  # Pass request in context
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})  # Pass request in context
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)'''


class FormViewSet(generics.ListCreateAPIView):
    queryset = Form.objects.all()  # Define the queryset for the list action
    serializer_class = FormSerializer  # Specify the serializer for this view
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]  # Define the permissions

    def get_queryset(self):
        # Optionally override this method to customize the queryset based on the request
        # For example, to only return the forms created by the authenticated user
        user = self.request.user
        return Form.objects.filter(author=user)  # Adjust this if you have a different ownership logic


class FromDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = FormSerializer
    queryset = Form.objects.filter()
    # lookup_field = 'id'

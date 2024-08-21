
# Create your views here.

from django.contrib.auth import login, authenticate, logout
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import Registerserializer, LoginSerializer


class LoginApiView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        """
        Login view to get user credentials
        """
        serializer = LoginSerializer(data=request.data, many=False)

        if serializer.is_valid():
            user = serializer.validated_data.get("user")
            if user is not None and user.is_active:
                login(request, user)
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterViewsetsApiView(generics.GenericAPIView):
    serializer_class = Registerserializer

    def post(self, request, *args, **kwargs):
        serializer = Registerserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user_name = serializer.validated_data['username']
            data = {
                'username': user_name
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutApiView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def post(self, request):
        # Log out the user
        logout(request)

        # Build the redirect URL to return
        redirect_url = request.build_absolute_uri('/form/home/')

        return Response({
            'message': 'Logged out successfully',
            'redirect_url': redirect_url
        }, status=status.HTTP_200_OK)

from django.urls import path,include
from rest_framework.authtoken import views
from django.contrib.auth.views import LogoutView
from .views import (
    RegisterViewsetsApiView,
    LoginApiView,
    LogoutApiView,
)


app_name = "api-v1"

urlpatterns = [
    # login user
    path("login/", LoginApiView.as_view(), name="login"),
    # logout user
    path("logout/", LogoutApiView.as_view(), name="logout"),
    # Registrations
    path("register/", RegisterViewsetsApiView.as_view(), name="register-users"),
    path("api/v2/", include("djoser.urls")),
    path("api/v2/", include("djoser.urls.jwt")),



    ]

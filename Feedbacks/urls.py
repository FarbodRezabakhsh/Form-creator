from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'Feedbacks'

urlpatterns = [
    path('questions/',views.QuestionListView.as_view(),name='question'),
    path('question/',views.QuestionCreateView.as_view(),name='question_create'),
    path('question/update/<int:pk>/',views.QuestionUpdateView.as_view(),name='question_update'),
    path('question/delete/<int:pk>/',views.QuestionDeleteView.as_view(),name='question_delete'),
]

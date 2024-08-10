from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'Feedbacks'

urlpatterns = [
    path('questions/',views.QuestionListView.as_view(),name='question'),
    path('question/',views.QuestionCreateView.as_view(),name='question_create'),
    path('question/update/<int:pk>/',views.QuestionUpdateView.as_view(),name='question_update'),
    path('question/delete/<int:pk>/',views.QuestionDeleteView.as_view(),name='question_delete'),
    path('answers/', views.AnswerListView.as_view(), name='answer_list'),
    path('answer/create/', views.AnswerCreateView.as_view(), name='answer_create'),
    path('answer/update/<int:pk>/', views.AnswerUpdateView.as_view(), name='answer_update'),
    path('answer/delete/<int:pk>/', views.AnswerDeleteView.as_view(), name='answer_delete'),
]

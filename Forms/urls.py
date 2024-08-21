from django.urls import path
from .views import FormViewSet, FromDetail

app_name = 'Forms'


urlpatterns = [
    path('', FormViewSet.as_view(), name='form_list'),
    path('detail_form/<int:pk>/', FromDetail.as_view(), name='form_detail'),
]

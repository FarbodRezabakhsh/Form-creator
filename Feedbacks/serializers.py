from rest_framework.serializers import ModelSerializer
from .models import Question,Answer

class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
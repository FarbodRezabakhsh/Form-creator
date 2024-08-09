from rest_framework import serializers
from .models import Answer,Question
# from .custom_relation import UserEmailNameSerializer
from django.contrib.auth.models import User

class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()
    # user = UserEmailNameSerializer(read_only=True)

    class Meta:
        model = Question
        fields = '__all__'

    def get_answers(self,obj):
        result = obj.answers.all()
        return AnswerSerializer(instance=result,many=True).data

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
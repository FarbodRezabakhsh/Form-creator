# forms/serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Form


class FormSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source='get_snippet')
    absolute_urls = serializers.SerializerMethodField()
    author = serializers.ReadOnlyField(source='author.username')  # Show only the username

    class Meta:
        model = Form
        fields = ['id', 'author', 'form_type', 'snippet', 'description', 'is_private', 'password',
                  'view_counts', 'user_answer_counts', 'absolute_urls']
        read_only_fields = ["author"]

    def get_absolute_urls(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(f'/detail_form/{obj.id}/')

    def to_representation(self, instance):
        request = self.context.get('request')
        rep = super().to_representation(instance)
        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('absolute_urls', None)
            rep.pop('snippet', None)
        else:
            rep.pop('description', None)
        return rep

    def validate(self, attrs):
        # Check if is_private is True and password is not provided
        if attrs.get('is_private') and not attrs.get('password'):
            raise serializers.ValidationError({'password': 'This field is required when is_private is True.'})
            # If is_private is False, set password to None
        if not attrs.get('is_private'):
            attrs['password'] = None  # or you can use attrs['password'] = ''

        return attrs

    def create(self, validated_data):
        # Directly assign the current user as the author
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)


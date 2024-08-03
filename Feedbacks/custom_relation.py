from rest_framework import serializers


class UserEmailNameSerializer(serializers.RelatedField):
    def to_representation(self, value):
        return f'{value.username} - {value.email}'

class FormTitleRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        return f'{value.description[:10]}'
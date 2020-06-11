from rest_framework import serializers
from tutorial.models import Tutorial
from tutorial import models
from django.contrib.auth.hashers import make_password


class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = (
            'id',
            'title',
            'description',
            'published',
            'author',
            'tutorial_image',
            'editor',
        )
        model = models.Tutorial

def validate_password(self, value: str) -> str:
    """
    Hash value passed by user.

    :param value: password of a user
    :return: a hashed version of the password
    """
    return make_password(value)


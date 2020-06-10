from rest_framework import serializers
from tutorial.models import Tutorial
from tutorial import models


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


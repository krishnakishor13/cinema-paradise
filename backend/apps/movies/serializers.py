from django.forms import ImageField
from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    Image= serializers.ImageField(
        allow_null= True
    )

    class Meta:
        model= Movie
        fields="__all__"
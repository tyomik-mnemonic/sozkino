from rest_framework import serializers
from .models import SozMovie
from django.conf import settings
from rest_framework import serializers, utils

class SozMovieSerializer(serializers.Serializer):
    model = SozMovie
    fields = [id, original_title, overview, budget, popularity, release_date, vore_average, original_language]

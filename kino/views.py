from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets, generics, permissions, filters, decorators
from .models import *

class MovieView(viewsets.ModelViewSet):
    queryset = SozMovie.objects.all()
    serializer_class = SozMovieSerializer
    permission_classes = (permissions.AllowAny,)

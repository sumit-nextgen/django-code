from email.mime import image
from django.shortcuts import render
from .models import media_upload
from.serializers import Usermedia
from rest_framework import viewsets

from fileupload import serializers

# Create your views here.

class mediaview (viewsets.ModelViewSet):
    queryset=media_upload.objects.all()
    serializer_class=Usermedia


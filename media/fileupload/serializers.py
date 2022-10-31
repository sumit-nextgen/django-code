
from rest_framework import serializers
from fileupload.models import media_upload


class Usermedia(serializers.HyperlinkedModelSerializer):
 
  class Meta:
    model =media_upload
    fields=['image','message']
    
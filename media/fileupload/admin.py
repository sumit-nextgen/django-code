from django.contrib import admin

# Register your models here.
from fileupload.models import media_upload


admin.site.register(media_upload)
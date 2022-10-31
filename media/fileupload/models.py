
from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File
from django_resized import ResizedImageField

#image compression method
def compress(image):
    im = Image.open(image)
    im_io = BytesIO() 
    im = im.resize( (320,640) )
    im.save(im_io, 'JPEG', quality=100) 
    new_image = File(im_io, name=image.name)
    return new_image

class media_upload(models.Model):
    
    
    image = models.ImageField('image/')
    message=models.CharField(max_length=100)
    def save(self, *args, **kwargs):                
        new_image =  compress(self.image)                
        self.image = new_image
        super().save(*args, **kwargs)

                    
        
    

    
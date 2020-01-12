from django.db import models
from time import time
class Im(models.Model):
    Image = models.ImageField(upload_to='pic_folder', default='pic_folder/none/no-img.jpg')

    def get_absolute_url(self):
        return time()
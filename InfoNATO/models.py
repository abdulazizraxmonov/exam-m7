from django.db import models
from django.contrib.auth.models import User

class InfoNATO(models.Model):
    photo = models.ImageField(upload_to='info_nato_photos')  
    name = models.CharField(max_length=100)  
    description = models.TextField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.name
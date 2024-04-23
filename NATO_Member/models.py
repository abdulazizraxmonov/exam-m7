from django.db import models
from django.contrib.auth.models import User

class NATO_Member(models.Model):
    name = models.CharField(max_length=100)
    year_joined = models.PositiveIntegerField()
    military_capability = models.CharField(max_length=100)
    budget_allocation = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    photo = models.ImageField(upload_to='member_photos/')
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
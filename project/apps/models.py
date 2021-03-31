from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    # additional
    def __str__(self):
        return self.username
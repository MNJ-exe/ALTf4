from django.db import models
from django.contrib.auth.models import User
from base.models import BaseModel
# Create your models here.
class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(default='', max_length=100)
    phoneno = models.CharField(default=0, max_length=100)
    gender = models.CharField( max_length=100)
    username = models.CharField(default='', max_length=100)
    email = models.CharField(default='', max_length=100)
    password = models.CharField(default='password', max_length=100)


    def _str_(self):
        return f'{self.user.username}'
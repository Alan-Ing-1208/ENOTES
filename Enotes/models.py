from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Signup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ContactNo = models.CharField(max_length=10, blank=True, null=True)
    About = models.CharField(max_length=450, blank=True, null=True)
    Role = models.CharField(max_length=150, blank=True, null=True)
    RegDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name


class Notes(models.Model):
    signup = models.ForeignKey(Signup, on_delete=models.CASCADE)
    Title = models.CharField(max_length=200, blank=True, null=True)
    Content = models.TextField(blank=True, null=True)  # Changed to TextField for longer content
    CreationDate = models.DateTimeField(auto_now_add=True)
    UpdationDate = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.Title

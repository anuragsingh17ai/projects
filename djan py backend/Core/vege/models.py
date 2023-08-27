from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Reciepe(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    recipe_name=models.CharField(max_length=50)
    recipe_description=models.TextField()
    recipe_image=models.ImageField(upload_to="reciepe")
    
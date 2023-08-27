from django.db import models

# Create your models here.
class Data(models.Model):
    recipe_name=models.CharField(max_length=50)
    recipe_desc=models.TextField()
    recipe_img=models.ImageField(upload_to='assets')
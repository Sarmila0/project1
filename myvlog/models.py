from django.db import models

# Create your models here.
class post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    # article=models.TextField()

    

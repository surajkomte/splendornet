from django.db import models

# Create your models here.
class reviewModel(models.Model):
    id=models.IntegerField(primary_key=True)
    movieTitle=models.CharField(max_length=200, null=False)
    director=models.CharField(null=False,max_length=100)
    reviewContent=models.CharField(max_length=500,null=False )
    rating=models.IntegerField(null=False)
    createaAt=models.DateField()
    reviewer_email_id=models.EmailField(unique=True)
    status=models.CharField(max_length=20)
    generes=models.CharField(max_length=40)
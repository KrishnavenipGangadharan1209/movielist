from django.db import models

# Create your models here.
class movlist(models.Model):
    moviename=models.CharField(max_length=150)
    moviedisc=models.TextField()
    Releaseyear=models.IntegerField()
    director=models.CharField(max_length=100)
    poster=models.ImageField(upload_to='pics')

    def __str__(self):
        return self.moviename
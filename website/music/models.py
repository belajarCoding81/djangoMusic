from django.db import models

# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=250)
    title = models.CharField(max_length=150)
    genre = models.CharField(max_length=50)
    logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.title + ' - '+ self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    fileType = models.CharField(max_length=50)
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title + ' - '+ self.fileType
    

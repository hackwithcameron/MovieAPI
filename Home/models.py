from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100, default="")
    thumbsUp = models.IntegerField()

    Movies = models.Manager()

    def __str__(self):
        return self.title

from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100, blank=False)
    id = models.IntegerField(blank=False, primary_key=True)
    thumbsUp = models.IntegerField()

    Movies = models.Manager()

    def __str__(self):
        return self.title

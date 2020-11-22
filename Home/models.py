from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100, blank=False)
    id = models.CharField(blank=False, primary_key=True, max_length=10)
    thumbsUp = models.IntegerField(default=0)
    thumbsDown = models.IntegerField(default=0)

    Movies = models.Manager()

    def __str__(self):
        return self.title

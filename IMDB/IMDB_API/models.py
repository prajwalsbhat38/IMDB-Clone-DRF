from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class StreamingPlatform(models.Model):
    name = models.CharField(max_length=25)
    about = models.CharField(max_length=200)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name

class WatchList(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=200)
    platform = models.ForeignKey(StreamingPlatform, on_delete=models.CASCADE, related_name='platform')
    active = models.BooleanField(default=True)
    avg_rating = models.FloatField(default=0)
    number_of_rating = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Reviews(models.Model):
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name='watchlist')
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    description = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.review_user.username)+ '|' +str(self.watchlist.title)+ '|' +str(self.rating)
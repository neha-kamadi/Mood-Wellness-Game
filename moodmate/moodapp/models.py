
# Create your models here.
from django.db import models

class MoodHistory(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField()
    mood = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.mood} ({self.score})"

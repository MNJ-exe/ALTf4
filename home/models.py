from django.db import models
from django.contrib.auth.models import User

class Content(models.Model):
    CATEGORY_CHOICES = [
        ('home', 'Home'),
        ('movie', 'Movie'),
        ('tvshow', 'TV Show'),
        ('documentary', 'Documentary')
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    release_date = models.DateField(null=True, blank=True)
    # Add other fields as needed (e.g., director, duration, etc.)

    def __str__(self):
        return self.title

from django.db import models
from django.contrib.auth.models import User
from home.models import Content

class Review(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.content.title} ({self.rating})"

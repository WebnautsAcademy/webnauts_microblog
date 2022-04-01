from django.db import models
from users.models import User


class Post(models.Model):
    file = models.FileField(upload_to='post_files/')
    title = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.title:
            return self.title
        return f"Post id: {self.id}"

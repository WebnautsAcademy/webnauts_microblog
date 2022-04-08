from django.db import models
from django.core.validators import FileExtensionValidator

from .validators import validate_size
from users.models import User


class ModelWithTS(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(ModelWithTS):
    file = models.FileField(upload_to='post_files/', validators=[validate_size])
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='posts')
    description = models.TextField(null=True, blank=True)
    likes = models.ManyToManyField(User)
    published = models.BooleanField(default=True)

    def __str__(self):
        if self.title:
            return self.title
        return f"Post id: {self.id}"


class Comment(ModelWithTS):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"user: {self.user.email}, comment: {self.title}"

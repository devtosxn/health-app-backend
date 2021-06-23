from django.db import models
from django.conf import settings
from .user import User
import uuid


class Blog(models.Model):
    DEFAULT_COVER_IMG_URL = "https://www.blogtyrant.com/wp-content/uploads/2017/02/how-to-write-a-good-blog-post.png"

    id = models.UUIDField(unique=True, primary_key=True,default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    cover_img = models.URLField(default=DEFAULT_COVER_IMG_URL)
    body = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    Artist = models.CharField(max_length=80)
    Artwork_Title = models.CharField(max_length=80)
    Comment_Box = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.Comment_Box, self.Artist)
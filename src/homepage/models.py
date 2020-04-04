from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
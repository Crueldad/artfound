from django.db import models

class Images(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
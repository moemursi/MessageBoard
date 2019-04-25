from django.db import models

# Create your models here.

class Post(models.Model):
    """Model definition for Post."""

    text = models.TextField()

    def __str__(self):
        return self.text[:50]

    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

   
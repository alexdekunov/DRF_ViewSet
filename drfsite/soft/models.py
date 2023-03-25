from django.db import models

# Create your models here.
class Soft(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    url = models.URLField()

    def __str__(self):
        return self.title



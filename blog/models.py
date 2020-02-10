from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=140, blank=False)
    text = models.CharField(max_length=1000, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

from django.db import models

# Create your models here.
class NewsModel(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.title
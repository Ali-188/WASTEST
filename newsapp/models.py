from django.db import models

# Create your models here
class News(models.Model):
    newstitle = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    date = models.CharField(max_length=128)
    description_text = models.CharField(max_length=128)

    def __str__(self):
        return self.newstitle

from django.db import models  # noqa F401

# your models here
class Pokemon(models.Model):
    title = models.TextField()
    def __str__(self):
        return '{}'.format(self.title)
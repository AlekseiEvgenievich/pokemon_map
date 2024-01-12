from django.db import models  # noqa F401

# your models here
class Pokemon(models.Model):
    title = models.TextField()
    photo = models.ImageField(blank=True)
    def __str__(self):
        return '{}'.format(self.title)


class PokemonEntity(models.Model):
	latttude = models.FloatField()         
	longitude = models.FloatField()
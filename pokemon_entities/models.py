from django.db import models  # noqa F401

# your models here
class Pokemon(models.Model):
    title = models.TextField()
    photo = models.ImageField(blank=True)
    def __str__(self):
        return '{}'.format(self.title)


class PokemonEntity(models.Model):
	pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
	latttude = models.FloatField()         
	longitude = models.FloatField()
	appeared_at = models.DateTimeField(null=True)
	disappeared_at = models.DateTimeField(null=True)
	level = models.IntegerField(null=True)
	health = models.IntegerField(null=True)
	attack = models.IntegerField(null=True)
	protection = models.IntegerField(null=True)
	endurance = models.IntegerField(null=True)
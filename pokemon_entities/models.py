from django.db import models 

class Pokemon(models.Model):
    title = models.TextField(verbose_name = "имя покемона")
    parent = models.ForeignKey(
        'self', 
        on_delete=models.SET_NULL, 
        verbose_name = "имя родителя",
        null=True, 
        blank=True, 
        related_name='evolutions'
    )
    title_en = models.TextField(verbose_name = "имя покемона на английском",blank=True)
    title_jp = models.TextField(verbose_name = "имя покемона на японском",blank=True)
    photo = models.ImageField(verbose_name = "фото покемона")
    description = models.TextField(verbose_name = "описание покемона",blank=True)  

    def __str__(self):
        return '{}'.format(self.title)


class PokemonEntity(models.Model):
	pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name = "имя покемона")
	latttude = models.FloatField(verbose_name = "широта")         
	longitude = models.FloatField(verbose_name = "долгота")
	appeared_at = models.DateTimeField(null=True, verbose_name = "время появляения")
	disappeared_at = models.DateTimeField(null=True, verbose_name = "время исчезновения")
	level = models.IntegerField(null=True, verbose_name = "уровень",blank=True)
	health = models.IntegerField(null=True, verbose_name = "сила",blank=True)
	attack = models.IntegerField(null=True, verbose_name = "атака",blank=True)
	protection = models.IntegerField(null=True, verbose_name = "зашита",blank=True)
	endurance = models.IntegerField(null=True, verbose_name = "урон",blank=True)
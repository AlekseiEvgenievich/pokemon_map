from django.db import models  # noqa F401

# your models here
class Pokemon(models.Model):
    title = models.TextField()
    title_en= models.TextField(default = 'Bulbausaur')
    title_jp= models.TextField(default = 'フシギダネ')
    photo = models.ImageField(blank=True)
    description = models.TextField(default = " маленький четвероногий покемон голубовато-зелёного цвета с темно-зелёными пятнами на теле. У него красные глаза, широкий рот и слегка заострённые уши. Когда его рот открыт, на его верхней челюсти видна пара заострённых зубов. У него толстые лапы, заканчивающиеся тремя острыми когтями. На спине у Бульбазавра находится зелёная луковица, которая, согласно записи в Покедексе, была посажена там при рождении. Когда Бульбазавр готов эволюционировать, луковица на его спине начинает мерцать голубоватым цветом и впоследствии преобразуется в бутон. Если он не хочет развиваться, он изо всех сил сопротивляется трансформации.")
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
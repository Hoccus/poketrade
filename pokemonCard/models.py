from django.db import models

# Create your models here.
class PokemonCard(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    hp = models.IntegerField()
    attack = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='pokemonCard_images/')
    def __str__(self):
        return str(self.id) + ' - ' + self.name
from django.db import models



# Create your models here.
class PokemonCard(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    description = models.TextField()
    image_url = models.URLField(default="https://via.placeholder.com/120")
    def __str__(self):
        return str(self.id) + ' - ' + self.name
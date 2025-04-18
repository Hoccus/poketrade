from django.db import models
from django.contrib.auth.models import User
from pokemonCard.models import PokemonCard

class CollectionItem(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    pokemon = models.ForeignKey(PokemonCard, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=255) #in collection/listed on marketplace/pending trade
    def __str__(self):
        return str(self.id) + ' - ' + self.user.username + ", " + self.pokemon.name

# Create your models here.

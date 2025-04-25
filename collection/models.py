from django.db import models
from django.contrib.auth.models import User
from pokemonCard.models import PokemonCard

class CollectionItem(models.Model):
    STATUS_CHOICES = [
        ('collection', 'In Collection'),
        ('listed', 'Listed on Marketplace'),
        ('pending', 'Pending Trade'),
    ]
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    pokemon = models.ForeignKey(PokemonCard, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='collection')
    def __str__(self):
        return str(self.id) + ' - ' + self.user.username + ", " + self.pokemon.name

# Create your models here.

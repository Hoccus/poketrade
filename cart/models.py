from django.db import models
from django.contrib.auth.models import User
from marketplace.models import MarketListing

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    total = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    def __str__(self):
        return str(self.id) + ' - ' + self.user.username

class CartItem(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order,
                              on_delete=models.CASCADE)
    marketListing = models.ForeignKey(MarketListing,
                              on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return str(self.id) + ' - ' + self.marketListing.item.pokemon.name



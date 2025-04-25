from django.db import models
from django.contrib.auth.models import User
from collection.models import CollectionItem

class MarketListing(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(CollectionItem, on_delete=models.CASCADE)
    price = models.FloatField()
    def __str__(self):
        return str(self.id) + ' - ' + self.seller.username








# Create your models here.

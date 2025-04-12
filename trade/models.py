from django.db import models
from django.contrib.auth.models import User
from collection.models import CollectionItem


class Trade(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    #initiatorItems = models.ForeignKey(CollectionItem, on_delete=models.CASCADE)
    #recipientItems = models.ForeignKey(CollectionItem, on_delete=models.CASCADE)
    initiator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='initiators')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipients')
    status = models.CharField(max_length=255)  # pending/completed
    def __str__(self):
        return str(self.id) + ' - ' + self.initiator.username + ", " + self.recipient.username

class TradeItem(models.Model):
    item = models.ForeignKey(CollectionItem, on_delete=models.CASCADE)
    trade = models.ForeignKey(Trade, on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.trade.id) + "-" + self.item.pokemon.name + ", " +self.recipient.username



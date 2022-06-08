from django.db import models

# Create your models here.

class Total_market_orders(models.Model):
    side = 'rsi'
    quantity = models.FloatField()

    def __str__(self):
        return self.side+'_'+self.quantity

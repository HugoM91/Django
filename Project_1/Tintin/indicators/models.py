from django.db import models

# Create your models here.

class RSI(models.Model):
    name = 'rsi'
    symbol = models.CharField(max_length=25)
    date = models.DateField()
    tf_1h = models.FloatField()
    tf_4h = models.FloatField()
    tf_1d = models.FloatField()
    def __str__(self):
        return self.name+'_'+self.symbol


class MOVINGAVG28(models.Model):
    name = 'mvgAVG_28'
    symbol = models.CharField(max_length=25)
    date = models.DateField()
    tf_1h = models.FloatField()
    tf_4h = models.FloatField()
    tf_1d = models.FloatField()
    def __str__(self):
        return self.name+'_'+self.symbol

class MOVINGAVG84(models.Model):
    name = 'mvgAVG_84'
    symbol = models.CharField(max_length=25)
    date = models.DateField()
    tf_1h = models.FloatField()
    tf_4h = models.FloatField()
    tf_1d = models.FloatField()
    def __str__(self):
        return self.name+'_'+self.symbol

class MOVINGAVG168(models.Model):
    name = 'mvgAVG_168'
    symbol = models.CharField(max_length=25)
    date = models.DateField()
    tf_1h = models.FloatField()
    tf_4h = models.FloatField()
    tf_1d = models.FloatField()
    def __str__(self):
        return self.name+'_'+self.symbol

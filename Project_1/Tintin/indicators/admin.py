from django.contrib import admin
from indicators.models import RSI,  MOVINGAVG28, MOVINGAVG84, MOVINGAVG168
# Register your models here.
admin.site.register(RSI)
admin.site.register(MOVINGAVG28)
admin.site.register(MOVINGAVG84)
admin.site.register(MOVINGAVG168)

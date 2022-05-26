from django.conf.urls import url
from . import views
from django.urls import path, include


app_name = 'market_orders'

urlpatterns= [
    path('market_orders/', views.market_orders, name="market_orders")

]

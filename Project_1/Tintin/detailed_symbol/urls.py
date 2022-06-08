from django.conf.urls import url
from . import views
from django.urls import path


app_name = 'detailed_symbol'

urlpatterns= [
    path('detailed_symbol/', views.detailed_symbol, name="detailed_symbol")
]

from django.conf.urls import url
from . import views
from django.urls import path


app_name = 'indicators'

urlpatterns= [
    path('indicators/', views.indicators, name="indicators")
]

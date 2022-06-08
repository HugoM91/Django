from django.conf.urls import url
from . import views
from django.urls import path, include


app_name = 'crud'

urlpatterns= [
    path('', views.RegistoListView.as_view(), name="crud"),
    path('', views.CRUD.as_view(), name="crud1"),
    path('create', views.RegistoCreateView.as_view(), name="create"),
    ]
"""path('crud/', views.CRUD.as_view(), name="crud"),"""

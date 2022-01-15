from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='usl'),
    path('prombez', views.prombez, name='prombez'),
    path('ates', views.ates, name='ates'),
    path('ispyt', views.ispyt, name='ispyt'),
    path('sootvet', views.sootvet, name='sootvet'),
    path('iso', views.iso, name='iso'),
    path('rad', views.rad, name='rad'),
    path('center', views.center, name='center'),
]

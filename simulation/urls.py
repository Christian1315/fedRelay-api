from django.urls import path

from . import views

urlpatterns= [
    path('create/',views.SimulationCreate.as_view(),name=''),
    path('',views.SimulationResult,name='')
]
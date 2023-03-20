from django.urls import path

from . import views

urlpatterns= [
    path('',views.EmailRegister.as_view(),name=''),
]
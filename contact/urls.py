from django.urls import path

from . import views

urlpatterns = [
    path('',views.ContactRegister.as_view(),name="Contact")
]
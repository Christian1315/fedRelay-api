from django.urls import path

from . import views

urlpatterns = [
    path('',views.PartenariatRegister.as_view(),name="partenariat")
]
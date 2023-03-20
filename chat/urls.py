from django.urls import path
from . import views

urlpatterns = [
    path("client", views.ClientMessageCreate.as_view(),name='client_chat'),
    path("<user_id>/client",views.GetAllClientMessage.as_view(),name="getmsg")
]
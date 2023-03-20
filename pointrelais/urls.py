from django.urls import path
from . import views

urlpatterns = [
    path("",views.GetAllRelayPoint.as_view(),name="relaypoints"),
    path("/<quartier_id>",views.GetAllRelayPointForUser.as_view(),name="")
]


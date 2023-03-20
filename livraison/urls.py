from django.urls import path
from . import views

urlpatterns = [
    # ====== USING GENERICS ====== #
    path('create',views.AddingOneDelivery.as_view()),
    path('<id>/update',views.UpdateOneDelivery.as_view(),name='updateDelivery'),
    path('<user_id>/deliveries',views.GetAllDelivery.as_view(),name='allDeliveries'),
    path('<str:follow_code>/followup',views.FollowUpDelivery.as_view())
]
from django.urls import path, include
from CUSTOMERAPP.API import views

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('customer',views.NewCustomer_Serializer_ListView)

urlpatterns = [
    path('',include(router.urls)),
]
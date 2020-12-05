from django.urls import path, include
from curdapp.api import views

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('emp',views.ProductDataView)

urlpatterns = [
    path('',include(router.urls)),
]
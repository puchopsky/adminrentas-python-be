
from django.urls import path, include
from .controller_views.OwnedPropertyView import OwnedPropertyView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('property', OwnedPropertyView)

urlpatterns = [
    path('', include(router.urls))
]

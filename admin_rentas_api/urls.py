
from django.urls import path, include
from .controller_views.OwnedPropertyView import OwnedPropertyView
from .controller_views.TokenValidationView import TokenValidationView
from rest_framework import routers
from django.conf.urls import url
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = routers.DefaultRouter()
router.register('property', OwnedPropertyView)

urlpatterns = [
    path('', include(router.urls)),
    url(r'token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    url(r'token/verify/$', TokenVerifyView.as_view(), name='token_verify'),
    url(r'token/validate/$', TokenValidationView.as_view(), name='token_validation'),
]

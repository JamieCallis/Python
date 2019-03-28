from rest_framework import routers
from backendapp.viewsets import SpacyViewSet

router = routers.DefaultRouter()

router.register(r'spacyapi', SpacyViewSet, base_name='spacyapi')


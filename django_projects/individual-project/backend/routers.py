from rest_framework import routers
from frontend.viewsets import SpacyViewSet

router = routers.DefaultRouter()

router.register(r'spacy-api', SpacyViewSet, base_name='spacy-api')


from rest_framework import routers
from frontend.viewsets import SpacyViewSet

router = routers.DefaultRouter()

router.register(r'spacy', SpacyViewSet, base_name='spacy_api')

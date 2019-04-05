from rest_framework import routers
from backendapp.viewsets import SpacyViewSet, BookMetaDataViewSet, BookTextViewSet

router = routers.DefaultRouter()

router.register(r'spacyapi', SpacyViewSet, base_name='spacyapi')
router.register(r'books', BookMetaDataViewSet, base_name='books')
router.register(r'book', BookTextViewSet, base_name='book')


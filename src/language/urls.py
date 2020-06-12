from django.urls import path
from rest_framework import routers
from .api.api import LanguageAPIView

router = routers.DefaultRouter(trailing_slash=False)
router.register('language', LanguageAPIView, 'language')

app_name    = 'language'
urlpatterns = router.urls

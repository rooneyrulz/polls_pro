from django.urls import path
from .api.api import (
    LanguageListAPI,
    LanguageCreateAPI,
    LanguageRetrieveAPI,
    LanguageUpdateAPIView,
    LanguageDestroyAPIView
)

app_name = 'language'
urlpatterns = [
    path('', LanguageListAPI.as_view(), name='language-list'),
    path('create/', LanguageCreateAPI.as_view(), name='language-create'),
    path('<int:pk>', LanguageRetrieveAPI.as_view(), name='language-retrieve'),
    path('<int:pk>/update/', LanguageUpdateAPIView.as_view(), name='language-update'),
    path('<int:pk>/destroy/', LanguageDestroyAPIView.as_view(), name='language-destroy'),

]

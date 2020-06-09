from django.urls import path
from .api.api import (FrameworkListAPI, FrameworkCreateAPI, FrameworkRetrieveAPI)

app_name    = 'framework'
urlpatterns = [
    path('', FrameworkListAPI.as_view(), name='list-framework'),
    path('<int:pk>/create/', FrameworkCreateAPI.as_view(), name='create-framework'),
    path('<int:pk>/', FrameworkRetrieveAPI.as_view(), name='retrieve-framework'),
]

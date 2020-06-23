from django.urls import path
from .api.api import RegisterAPIView

app_name = 'account'
urlpatterns = [
    path('register', RegisterAPIView.as_view(), name='register'),
]

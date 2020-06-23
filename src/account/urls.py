from django.urls import path
from .api.api import RegisterAPIView, AuthenticateAPIView, UserAPIView

app_name = 'account'
urlpatterns = [
    path('register', RegisterAPIView.as_view(), name='register'),
    path('login', AuthenticateAPIView.as_view(), name='authenticate'),
    path('user', UserAPIView.as_view(), name='auth_user'),
]

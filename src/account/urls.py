from django.urls import path
from knox import views as knox_view
from .api.api import RegisterAPIView, AuthenticateAPIView, UserAPIView

app_name = 'account'
urlpatterns = [
    path('register', RegisterAPIView.as_view(), name='register'),
    path('login', AuthenticateAPIView.as_view(), name='authenticate'),
    path('user', UserAPIView.as_view(), name='auth_user'),
    path('logout', knox_view.LogoutView.as_view(), name='knox_logout'),
]

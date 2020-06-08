from django.urls import path
from .api.api import GetFrameworks

app_name = 'framework'
urlpatterns = [
    path('', GetFrameworks.as_view(), name='list-framework'),
]

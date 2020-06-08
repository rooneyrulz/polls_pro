from django.urls import path
from .api.api import GetFrameworks

app_name = 'framework'
urlpatterns = [
    path('choices/', GetFrameworks, name='list-framework'),
]

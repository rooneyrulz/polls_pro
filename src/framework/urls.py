from django.urls import path
from .api.api import (
    GetChoices,
)

app_name = 'framework'
urlpatterns = [
    path('choices/', GetChoices.as_view(), name='list-framework'),
]

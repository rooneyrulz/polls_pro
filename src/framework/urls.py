from django.urls import path
from .api.api import (
    FrameworkListAPI,
    FrameworkCreateAPI,
    FrameworkRetrieveAPI,
    FrameworkUpdateAPI,
    FrameworkDestroyAPI,
    FrameworkCreateVoteAPI
)

app_name    = 'framework'
urlpatterns = [
    path('', FrameworkListAPI.as_view(), name='list-framework'),
    path('<int:pk>', FrameworkRetrieveAPI.as_view(), name='retrieve-framework'),
    path('<int:pk>/destroy', FrameworkDestroyAPI.as_view(), name='destroy-framework'),
    path('<int:language_pk>/create', FrameworkCreateAPI.as_view(), name='create-framework'),
    path('<int:language_pk>/<int:pk>/update', FrameworkUpdateAPI.as_view(), name='update-framework'),
    path('<int:language_pk>/<int:pk>/vote', FrameworkCreateVoteAPI.as_view(), name='create-vote-framework'),
]

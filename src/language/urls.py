from django.urls import path
from .api.api import (
    GetPolls,
    GetPoll,
    GetChoices,
    PollListAPI,
    PollCreateAPI,
    PollRetrieveAPI,
    PollUpdateAPIView,
    PollDestroyAPIView
)

app_name = 'language'
urlpatterns = [
    path('', PollListAPI.as_view(), name='language-list'),
    path('create/', PollCreateAPI.as_view(), name='language-create'),
    path('choices/', GetChoices.as_view(), name='get_choices'),
    path('<int:pk>', PollRetrieveAPI.as_view(), name='language-retrieve'),
    path('<int:pk>/update/', PollUpdateAPIView.as_view(), name='language-update'),
    path('<int:pk>/destroy/', PollDestroyAPIView.as_view(), name='language-destroy'),

]

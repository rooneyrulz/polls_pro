from django.urls import path
from .views import (
    GetPolls,
    GetPoll,
    GetChoices,
    PollListAPI,
    PollCreateAPI,
    PollRetrieveAPI,
    PollUpdateAPIView,
    PollDestroyAPIView
)

app_name = 'poll'
urlpatterns = [
    path('', PollListAPI.as_view(), name='poll-list'),
    path('create/', PollCreateAPI.as_view(), name='poll-create'),
    path('choices/', GetChoices.as_view(), name='get_choices'),
    path('<int:pk>', PollRetrieveAPI.as_view(), name='poll-retrieve'),
    path('<int:pk>/update/', PollUpdateAPIView.as_view(), name='poll-update'),
    path('<int:pk>/destroy/', PollDestroyAPIView.as_view(), name='poll-destroy'),

]

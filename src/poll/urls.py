from django.urls import path

from .views import GetPolls, GetPoll, GetChoices

app_name = 'poll'
urlpatterns = [
    path('', GetPolls.as_view(), name='get_polls'),
    path('choices/', GetChoices.as_view(), name='get_choices'),
    path('<int:pk>', GetPoll.as_view(), name='get_poll'),
]

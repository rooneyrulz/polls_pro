from django.urls import path

from .views import GetPolls

app_name = 'poll'
urlpatterns = [
    path('', GetPolls.as_view(), name='get_polls'),
]

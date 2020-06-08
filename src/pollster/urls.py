from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/language/', include('language.urls', namespace='language')),
    path('api/framework/', include('framework.urls', namespace='framework'))
]

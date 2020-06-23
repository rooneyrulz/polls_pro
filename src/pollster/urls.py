from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('language.urls', namespace='language')),
    path('api/framework/', include('framework.urls', namespace='framework')),
    path('api/account/', include('account.urls', namespace='account')),
]

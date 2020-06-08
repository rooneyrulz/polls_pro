from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from language.serializer import LanguageSerializer
from language.models import Language

class LanguageListAPI(ListAPIView):
    queryset            = Language.objects.all()
    serializer_class    = LanguageSerializer

class LanguageCreateAPI(CreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class LanguageRetrieveAPI(RetrieveAPIView):
    queryset            = Language.objects.all()
    serializer_class    = LanguageSerializer
    # lookup_field = 'id'

class LanguageUpdateAPIView(UpdateAPIView):
    queryset            = Language.objects.all()
    serializer_class    = LanguageSerializer

class LanguageDestroyAPIView(DestroyAPIView):
    queryset            = Language.objects.all()
    serializer_class    = LanguageSerializer

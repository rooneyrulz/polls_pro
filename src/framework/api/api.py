from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from framework.serializer import FrameworkSerializer
from framework.models import Framework
from language.models import Language

class LanguageObjectMixin(object):
    def get_language_object(self, id=None):
        return get_object_or_404(Language, pk=id)


class FrameworkListAPI(ListAPIView):
    queryset            = Framework.objects.all()
    serializer_class    = FrameworkSerializer

class FrameworkRetrieveAPI(RetrieveAPIView):
    queryset            = Framework.objects.all()
    serializer_class    = FrameworkSerializer

class FrameworkCreateAPI(LanguageObjectMixin, CreateAPIView):
    queryset            = Framework.objects.all()
    serializer_class    = FrameworkSerializer

    def perform_create(self, serializer):
        serializer.save(language=self.get_language_object(id=self.kwargs.get('pk')))

class GetFrameworks(APIView):
    
    def get(self, request, *args, **kwargs):
        queryset = Framework.objects.all()
        serializer = FrameworkSerializer(queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = FrameworkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

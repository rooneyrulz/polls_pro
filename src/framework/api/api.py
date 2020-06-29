from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)

from framework.serializer import FrameworkSerializer
from framework.models import Framework
from language.models import Language

class LanguageObjectMixin(object):
    def get_language_object(self, id=None):
        return get_object_or_404(Language, pk=id)

class FrameworkObjectMixin(object):
    def get_framework_object(self, id=None):
        return get_object_or_404(Framework, pk=id)


class FrameworkListAPI(ListAPIView):
    queryset            = Framework.objects.all()
    serializer_class    = FrameworkSerializer

class FrameworkRetrieveAPI(RetrieveAPIView):
    queryset            = Framework.objects.all()
    serializer_class    = FrameworkSerializer
    permission_classes  = [permissions.IsAuthenticated]

class FrameworkCreateAPI(LanguageObjectMixin, CreateAPIView):
    queryset            = Framework.objects.all()
    serializer_class    = FrameworkSerializer
    permission_classes  = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(language=self.get_language_object(id=self.kwargs.get('language_pk')))


class FrameworkUpdateAPI(LanguageObjectMixin, UpdateAPIView):
    queryset            = Framework.objects.all()
    serializer_class    = FrameworkSerializer
    permission_classes  = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(language=self.get_language_object(id=self.kwargs.get('language_pk')))


class FrameworkDestroyAPI(DestroyAPIView):
    queryset            = Framework.objects.all()
    serializer_class    = FrameworkSerializer
    permission_classes  = [permissions.IsAuthenticated]

# class FrameworkCreateVoteAPI(
#     LanguageObjectMixin,
#     FrameworkObjectMixin,
#     UpdateAPIView):
#     queryset            = Framework.objects.all()
#     serializer_class    = FrameworkSerializer
#     permission_classes  = [permissions.IsAuthenticated]

#     def get_object(self, *args, **kwargs):
#         if self.get_language_object(id=self.kwargs.get('language_pk')):
#             return self.get_framework_object(id=self.kwargs.get('pk'))

#     def perform_update(self, serializer):
#         serializer.save(
#             name=self.get_object().name,
#             language=self.get_language_object(id=self.kwargs.get('language_pk')),
#             vote=self.get_object().vote + 1,
#         )


class FrameworkCreateVoteAPI(UpdateAPIView):
    queryset            = Framework.objects.all()
    serializer_class    = FrameworkSerializer
    permission_classes  = [permissions.IsAuthenticated]

    # def get_object(self, *args, **kwargs):
    #     return get_object_or_404(Framework, pk=self.kwargs.get('pk'))

    def perform_update(self, serializer):
        serializer.validated_data['vote'].append(self.request.user)
        serializer.save()

        

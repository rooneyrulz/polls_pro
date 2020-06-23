from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.auth import AuthToken

from account.serializer import UserSerializer, RegisterSerializer, LoginSerializer


# REGISTER API VIEW
class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(
                user,
                context=self.get_serializer_context()
            ).data,
            "token": AuthToken.objects.create(user)[1],
        })


# AUTHENTICATE API VIEW
class AuthenticateAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(
                user,
                context=self.get_serializer_context()
            ).data,
            "token": AuthToken.objects.create(user)[1],
        })


# USER API VIEW
class UserAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_object(self, *args, **kwargs):
        return self.request.user
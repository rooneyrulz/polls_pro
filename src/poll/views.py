from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from .serializer import QuestionSerializer, ChoiceSerializer
from .models import Question, Choice

class GetPolls(APIView):

    def get(self, request, *args, **kwargs):
        queryset = Question.objects.all()
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

            


class GetPoll(APIView):
    def get(self, request, pk=None, *args, **kwargs):
        obj = Question.objects.get(pk=pk)
        serializer = QuestionSerializer(obj)
        return Response(serializer.data, status=HTTP_200_OK)


class GetChoices(APIView):
    
    def get(self, request, *args, **kwargs):
        queryset = Choice.objects.all()
        serializer = ChoiceSerializer(queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = ChoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

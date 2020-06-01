from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED

from .serializer import QuestionSerializer, ChoiceSerializer
from .models import Question, Choice

class GetPolls(APIView):

    def get(self, request, *args, **kwargs):
        queryset = Question.objects.all()
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        pass
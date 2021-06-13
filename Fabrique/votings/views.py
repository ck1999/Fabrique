# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

from .models import Voting, VoteVariant_Type2

from .serializers import VotingSerializer, VoteSerializer

class VotingsList(APIView): #Список активных голосований и добавление новых
    queryset = Voting.objects.all()
    serializer_class = VotingSerializer

    def get(self, request):
        votings = Voting.objects.all().filter(is_active=True)
        serializer = self.serializer_class(votings, many=True)
        return Response(serializer.data)

    def post(self, request):

        if request.user.id == None:
            return Response(status=401)

        context = {
            "request": self.request,
        }

        serializer = self.serializer_class(data=request.data, context=context)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        return JsonResponse(serializer.errors, status=400)

class VotingDetail(APIView): #Получение и обновление голосования по ID

    serializer_class = VotingSerializer

    def get(self, request, pk):
        try:
            voting = Voting.objects.get(pk=pk)
        except Voting.DoesNotExist:
            return JsonResponse(status=400)
        serializer = self.serializer_class(voting)
        return Response(serializer.data)

    def put(self, request, pk):
        serializer = self.serializer_class(pk, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class VotesList(APIView):

    serializer_class = VoteSerializer

    def get(self, request):
        votes = VoteVariant_Type2.objects.all()
        serializer = self.serializer_class(votes, many=True)
        return Response(serializer.data)


class VoteDetail(APIView):

    serializer_class = VoteSerializer

    def get(self, request, pk):
        try:
            voting = VoteVariant_Type2.objects.get(pk=pk)
        except VoteVariant_Type2.DoesNotExist:
            return Response(status=400)
        serializer = self.serializer_class(voting)
        return Response(serializer.data)
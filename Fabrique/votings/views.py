# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

from .models import Voting, Choice, VoteFact
from .serializers import VotingSerializer, ChoicesSerializer, VotesSerializer

class VotingsList(APIView): #Список активных голосований и добавление новых
    queryset = Voting.objects.all()
    serializer_class = VotingSerializer

    def get(self, request):
        votings = Voting.objects.all().filter(is_active=True)
        serializer = self.serializer_class(votings, many=True)
        return Response(serializer.data, status=201)

    def post(self, request):

        if request.user.id == None:
            return Response(status=401)

        context = {
            "request": self.request,
        }

        serializer = self.serializer_class(data=request.data, context=context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class VotingDetail(APIView): #Получение и обновление голосования по ID

    serializer_class = VotingSerializer

    def get(self, request, pk):
        try:
            voting = Voting.objects.get(pk=pk)
        except Voting.DoesNotExist:
            return JsonResponse(status=400)
        serializer = self.serializer_class(voting)
        return Response(serializer.data, status=201)

    def put(self, request, pk):
        serializer = self.serializer_class(pk, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class ChoicesList(APIView): #Список списка вариантов выбора

    serializer_class = ChoicesSerializer

    def get(self, request):
        choices = Choice.objects.all()
        serializer = self.serializer_class(choices, many=True)
        return Response(serializer.data, status=201)

    def post(self, request):
        
        if request.user.id == None:
            return Response(status=401)

        context = {
            "request": self.request,
        }

        serializer = self.serializer_class(data=request.data, context=context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class ChoiceDetail(APIView): #Получение и обновление "выбора" по ID

    serializer_class = ChoicesSerializer

    def get(self, request, pk):
        try:
            choice = Choice.objects.get(pk=pk)
        except Choice.DoesNotExist:
            return JsonResponse(status=400)
        serializer = self.serializer_class(choice)
        return Response(serializer.data, status=201)

    def put(self, request, pk):
        serializer = self.serializer_class(pk, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class VotesList(APIView): #Список всех выборов

    serializer_class = VotesSerializer

    def get(self, request):
        votes = VoteFact.objects.all()
        serializer = self.serializer_class(votes, many=True)
        return Response(serializer.data, status=201)

    def post(self, request):
        
        if request.user.id == None:
            return Response(status=401)

        context = {
            "request": self.request,
        }

        serializer = self.serializer_class(data=request.data, context=context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class VoteDetail(APIView): #Получение и обновление определенного выбора по ID

    serializer_class = VotesSerializer

    def get(self, request, pk):
        try:
            vote = VoteFact.objects.get(pk=pk)
        except VoteFact.DoesNotExist:
            return JsonResponse(status=400)
        serializer = self.serializer_class(vote)
        return Response(serializer.data, status=201)

    def put(self, request, pk):
        serializer = self.serializer_class(pk, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
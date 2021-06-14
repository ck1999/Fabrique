from django.urls import path
from .views import VoteDetail, VotingsList, VotingDetail, ChoicesList, ChoiceDetail, VotesList

urlpatterns = [
    path('', VotingsList.as_view()),
    path('<int:pk>', VotingDetail.as_view()),
    path('votes', VotesList.as_view()),
    path('votes/<int:pk>', VoteDetail.as_view()),
    path('choices', ChoicesList.as_view()),
    path('choices/<int:pk>', ChoiceDetail.as_view())
]
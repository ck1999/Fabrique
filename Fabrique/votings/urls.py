from django.urls import path
from .views import VoteDetail, VotingsList, VotingDetail, VotesList

urlpatterns = [
    path('', VotingsList.as_view()),
    path('<int:pk>', VotingDetail.as_view()),
    path('votes', VotesList.as_view()),
    path('votes/<int:pk>', VoteDetail.as_view())
]
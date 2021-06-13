from django.conf import settings
from django.urls import path
from django.urls.conf import include
from .views import CreateUserView, UserProfile

urlpatterns = [
    path('profile', UserProfile.as_view()),
    path('sign_up', CreateUserView.as_view()),
    path('', include('rest_framework.urls', namespace='rest_framework'))
]
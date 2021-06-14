from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Voting(models.Model):

    class MetaTypeChoice(models.IntegerChoices):
        first = 1
        second = 2
        third = 3

    author = models.ForeignKey(to=User, on_delete=models.CASCADE, editable=False)
    title = models.TextField()
    description = models.TextField()
    type = models.IntegerField(choices=MetaTypeChoice.choices, default=MetaTypeChoice.first, editable=False)
    total_choices = models.IntegerField(default=1)
    published = models.DateTimeField(auto_now_add=True, editable=False)
    finished = models.DateTimeField()
    is_active = models.BooleanField(default=True)

class Choice(models.Model):
    
    voting = models.ForeignKey(to=Voting, on_delete=models.CASCADE)
    text = models.CharField(max_length=64)
    total_votes = models.IntegerField(default=0)

class VoteFact(models.Model):

    choice = models.ForeignKey(to=Choice, on_delete=models.CASCADE)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model

# Create your models here.
class Voting(models.Model):

    class TypeVariants(models.IntegerChoices):
        first = 1
        second = 2
        third = 3

    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()
    type = models.IntegerField(choices=TypeVariants.choices, default=TypeVariants.first) #editable=False
    published = models.DateTimeField(auto_now_add=True, editable=False)
    finished = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-finished']

class VoteVariant_Type1(models.Model):
    voting = models.ForeignKey(to=Voting, on_delete=models.CASCADE)
    description = models.TextField()

class VoteVariant_Type2(models.Model):
    voting = models.ForeignKey(to=Voting, on_delete=models.CASCADE)
    
    class CheckBoxes(models.Choices):
        first = 'FR'
        second = 'SC'
        third = 'TH'

    description = models.CharField(max_length=2,choices=CheckBoxes.choices, default=CheckBoxes.first)

class VoteVariant_Type3(models.Model):
    voting = models.ForeignKey(to=Voting, on_delete=models.CASCADE)

    class RadioBoxes(models.Choices):
        first = 'FR'
        second = 'SC'
        third = 'TH'

    description = models.CharField(max_length=2,choices=RadioBoxes.choices, default=RadioBoxes.first)
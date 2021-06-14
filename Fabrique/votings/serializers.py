from rest_framework import serializers
from datetime import date
from .models import Voting, Choice, VoteFact

class VotingSerializer(serializers.ModelSerializer):

    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=100)
    type = serializers.ChoiceField(choices=[1,2,3])
    total_choices = serializers.IntegerField(default=1)
    published = serializers.DateTimeField(default=date.today(), read_only=True)
    finished = serializers.DateTimeField()
    is_active = serializers.BooleanField(default=True, read_only=True)

    class Meta:
        model = Voting
        fields = '__all__'

    def create(self, validated_data):
        voting = Voting(**validated_data)
        voting.save()
        
        if validated_data['type'] == 2:
            for i in range(voting.total_choices):
                __choice = Choice(voting=voting, text=f'VID: {voting.id}')
                __choice.save()

        return voting

    def update(self, pk, validated_data):
        voting = Voting(id=pk, **validated_data)
        voting.save()
        
        return voting

class ChoicesSerializer(serializers.ModelSerializer):

    voting = serializers.PrimaryKeyRelatedField(queryset=Voting.objects.all().filter(is_active=True))

    class Meta:
        model = Choice
        fields = '__all__'

    def create(self, validated_data):
        choice = Choice(**validated_data)
        choice.save()

        return choice

    def update(self, pk, validated_data):
        choice = Choice(id=pk, **validated_data)
        choice.save()

        return choice

class VotesSerializer(serializers.ModelSerializer):

    choice = serializers.PrimaryKeyRelatedField(queryset=Choice.objects.all())
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = VoteFact
        fields = '__all__'

    def create(self, validated_data):
        vote = VoteFact(**validated_data)
        vote.save()

        choice = Choice.objects.get(id=validated_data['choice'].id)
        choice.total_votes += 1
        choice.save()
        
        return vote

    def update(self, pk, validated_data):
        vote = VoteFact(id=pk, **validated_data)
        vote.save()

        return vote
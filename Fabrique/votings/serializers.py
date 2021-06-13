from rest_framework import serializers

from django.shortcuts import get_object_or_404

from datetime import date

from .models import Voting, VoteVariant_Type1, VoteVariant_Type2, VoteVariant_Type3

class VotingSerializer(serializers.ModelSerializer):

    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=100)
    type = serializers.ChoiceField(choices=[1,2,3])
    published = serializers.DateTimeField(default=date.today(), read_only=True)
    finished = serializers.DateTimeField()
    is_active = serializers.BooleanField(default=True, read_only=True)

    class Meta:
        model = Voting
        fields = '__all__'

    def create(self, validated_data):
        voting = Voting(**validated_data)
        voting.save()
        if validated_data['type'] == 1:
            type = VoteVariant_Type1(voting=voting, description='WOW')
        elif validated_data['type'] == 2:
            type = VoteVariant_Type2(voting=voting)
        else:
            type = VoteVariant_Type3(voting=voting)

        type.save()

        return voting

    def update(self, pk, validated_data):
        voting = Voting(id=pk, **validated_data)
        voting.save()
        
        return voting

class VoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = VoteVariant_Type2
        fields = '__all__'

    def create(self, pk, validated_data):
        voting = get_object_or_404(VoteVariant_Type1, id=pk) or get_object_or_404(VoteVariant_Type2, id=pk) or get_object_or_404(VoteVariant_Type3, id=pk)
        pass
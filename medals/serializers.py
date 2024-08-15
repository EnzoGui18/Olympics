from rest_framework import serializers
from .models import Country, Medal, Sport

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['name', 'gold_medals', 'silver_medals', 'bronze_medals']

class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = ['name']

class MedalSerializer(serializers.ModelSerializer):
    sport = SportSerializer()

    class Meta:
        model = Medal
        fields = ['sport', 'gold_medals', 'silver_medals', 'bronze_medals']

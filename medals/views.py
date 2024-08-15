from rest_framework import generics
from .models import Country, Medal
from .serializers import CountrySerializer, MedalSerializer

class CountryMedalDetailView(generics.RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_field = 'name'

class CountrySportsMedalsView(generics.ListAPIView):
    serializer_class = MedalSerializer

    def get_queryset(self):
        country_name = self.kwargs['name']
        return Medal.objects.filter(country__name=country_name)

class Top20CountriesView(generics.ListAPIView):
    serializer_class = CountrySerializer

    def get_queryset(self):
        return Country.objects.all().order_by('-gold_medals', '-silver_medals', '-bronze_medals')[:20]

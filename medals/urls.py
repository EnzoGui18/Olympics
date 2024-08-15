from django.urls import path
from .views import CountryMedalDetailView, CountrySportsMedalsView, Top20CountriesView

urlpatterns = [
    path('api/medals/<str:name>/', CountryMedalDetailView.as_view(), name='country-medals'),
    path('api/medals/<str:name>/sports/', CountrySportsMedalsView.as_view(), name='country-sports-medals'),
    path('api/medals/top-20/', Top20CountriesView.as_view(), name='top-20-countries'),
]

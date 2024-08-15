from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    gold_medals = models.IntegerField(default=0)
    silver_medals = models.IntegerField(default=0)
    bronze_medals = models.IntegerField(default=0)

    def total_medals(self):
        return self.gold_medals + self.silver_medals + self.bronze_medals

    def __str__(self):
        return self.name

class Sport(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Medal(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    gold_medals = models.IntegerField(default=0)
    silver_medals = models.IntegerField(default=0)
    bronze_medals = models.IntegerField(default=0)

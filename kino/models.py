from django.db import models
from dataclasses import dataclass



@dataclass
class DataReq:
    link: str
    api_key: str
  
test = DataReq('https://api.themoviedb.org/3/movie/550?api_key=', '47de4c8f17d0051399ce16d5edf26555')

def conc():
        print (test.link+test.api_key)

print(conc())

class SozMovie(models.Model):
    id = models.IntegerField(primary_key=True)
    original_title = models.TextField()
    overview = models.TextField()
    budget = models.IntegerField()
    popularity = models.FloatField()
    #release_date = models.DataField()
    vote_average = models.FloatField()
    original_language = models.TextField()

    class Meta:
        managed = True
        verbose_name = 'фильм'
        verbose_name = 'фильмы'
        
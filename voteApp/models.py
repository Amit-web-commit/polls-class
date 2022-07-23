
from django.db import models

# Create your models here.
class Candidate(models.Model):
    id=models.IntegerField(primary_key=True)
    name= models.CharField(max_length=100)
    vote_count=models.IntegerField(default=1)

    def __str__(self):
        return self.name
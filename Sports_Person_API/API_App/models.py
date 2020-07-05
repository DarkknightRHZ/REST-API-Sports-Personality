from django.db import models

# Create your models here.

class Sports_person (models.Model):
    person_id = models.IntegerField(default=-1)
    name = models.CharField(max_length=60, default='John Doe')
    sport = models.CharField(max_length=60, default='NR')

    def __str__(self):
        return self.name
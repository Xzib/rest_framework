from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    date_added = models.DateField()

    def __str__(self):
        return f'{self.name} added on {self.date_added}'


""" Models of todo app """
from django.db import models

class List(models.Model):
    """ List model of todo app """
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.item} | {str(self.completed)}'

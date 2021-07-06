from django.db import models

# Create your models here.
class Book(models.Model):
    Book_name=models.CharField(max_length=200)
    Author=models.CharField(max_length=200)
    Genre=models.CharField(max_length=200)
    Language=models.CharField(max_length=200)

    def __str__(self):
        return self.Book_name
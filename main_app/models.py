from django.db import models

# Create your models here.

# models.Model we inherit from which will give our models the ability to perform 
# CRUD updates on a table in sql (in this case)
class Cat(models.Model):
    # define the columns, and the datatypes enforeced in each row
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name
from django.db import models
from django.urls import reverse

#import the User model
from django.contrib.auth.models import User
# Create your models here.

# Add the Toy model
class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('toy-detail', kwargs={'pk': self.id})


# models.Model we inherit from which will give our models the ability to perform 
# CRUD updates on a table in sql (in this case)
class Cat(models.Model):
    # define the columns, and the datatypes enforeced in each row
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    # django adds the _id for us!
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # add our many to many relationship
    toys = models.ManyToManyField(Toy)

    def get_absolute_url(self):
        # self.id refers to the cat your just created
        # refers to the primary key on the row you just added 
        # to the cats table
        # reverse takes the name of url
        # cat_id is coming from the param name in cats-d
        return reverse('cats-detail', kwargs={'cat_id': self.id})

    def __str__(self):
        return self.name

# all caps tells other python developers don't change this 
# variable (python convention)
MEALS = (
    ("B", "Breakfast"),
    ("L", "Lunch"),
    ("D", "Dinner"),
) 

# to define the many side after the one
class Feeding(models.Model):
    date = models.DateField()
    # select menu (Dropdown)
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0] # B is the default value
    )

    # create a cat_id in psql on the feeding_table, django
    # automatically ads the _id
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        # self.get_<propertynamethathasthechoices>_display()
        return f"{self.get_meal_display()} on {self.date}"

    class Meta:
        # lookup different attributes from docs
        ordering = ['-date'] # newest feeding first when displayed





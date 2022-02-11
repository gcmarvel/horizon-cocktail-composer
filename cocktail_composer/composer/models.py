from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from .choices import UNIT_CHOICES, ICE_CHOICES


class Cocktail(models.Model):
    name = models.CharField(max_length=40, null=True)
    image = models.ImageField(null=True, blank=True)
    sweet = models.IntegerField(default=0,
                                validators=[
                                    MaxValueValidator(5),
                                    MinValueValidator(0)
                                ])
    sour = models.IntegerField(default=0,
                               validators=[
                                   MaxValueValidator(5),
                                   MinValueValidator(0)
                               ])
    bitter = models.IntegerField(default=0,
                                 validators=[
                                     MaxValueValidator(5),
                                     MinValueValidator(0)
                                 ])
    spicy = models.IntegerField(default=0,
                                validators=[
                                    MaxValueValidator(5),
                                    MinValueValidator(0)
                                ])
    fresh = models.IntegerField(default=0,
                                validators=[
                                    MaxValueValidator(5),
                                    MinValueValidator(0)
                                ])
    citrus = models.IntegerField(default=0,
                                 validators=[
                                     MaxValueValidator(5),
                                     MinValueValidator(0)
                                 ])
    creamy = models.IntegerField(default=0,
                                 validators=[
                                     MaxValueValidator(5),
                                     MinValueValidator(0)
                                 ])
    coffee = models.IntegerField(default=0,
                                 validators=[
                                     MaxValueValidator(5),
                                     MinValueValidator(0)
                                 ])
    ice = models.CharField(max_length=20, choices=ICE_CHOICES, default='cubes')

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=40, null=False)
    alc = models.IntegerField(default=0,
                              validators=[
                                  MaxValueValidator(96),
                                  MinValueValidator(0)
                              ])
    sugar = models.IntegerField(default=0)
    garnish = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class IngredientVolume(models.Model):
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE,
                                 related_name='ingredients')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    volume = models.IntegerField(validators=[
        MaxValueValidator(300),
        MinValueValidator(0)
    ])
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES, default='ml')

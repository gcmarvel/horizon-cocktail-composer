from django.contrib import admin
from .models import Cocktail, Ingredient, IngredientVolume


class IngredientsInline(admin.TabularInline):
    model = IngredientVolume


class CocktailAdmin(admin.ModelAdmin):
    inlines = [
        IngredientsInline
    ]

admin.site.register(Cocktail, CocktailAdmin)
admin.site.register(Ingredient)

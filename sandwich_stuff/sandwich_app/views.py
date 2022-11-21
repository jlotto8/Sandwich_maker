from django.shortcuts import render
from  django.views import View

import random


ingredients = {
    'meats': ['turkey', 'salami', 'pepperoni', 'sliced chicken', 'pastrami', 'tuna', 'veggie burger', 'ham'],
    'cheeses': ['provolone', 'american', 'cheddar', 'swiss', 'pepper jack', 'fondue'],
    'toppings': ['lettuce', 'tomato', 'banana peppers', 'hot peppers', 'onions', 'olives', 'spinach', 'avocado', 'cucumber', 'cream cheese', 'relish']
    }

class SandwichappView(View):
    def get(self, request):
        return render (
            request = request, 
            template_name  = 'sandwichapp.html',
            context = {'ingredients': ingredients.keys()}
        )

class IngredientsView(View):
    def get(self, request, ingredient_type):
        return render(
            request = request,
            template_name = 'ingredients_list.html',
            context = {
                'ingredients': ingredients[ingredient_type],
                'ingredient_type': ingredient_type
            }
        ),

class SampleSandwichView(View):
    def get(self, request):
        return render (
            request = request,
            template_name = 'sample_sandwich.html',
            context = {
                'meat': random.choice(ingredients['meats']),
                'cheese': random.choice(ingredients['cheeses']),
                'topping': random.choice(ingredients['toppings']),
            }
        ),

class EntireMenuView(View):
    def get(self, request):
        return render (
            request = request,
            template_name = 'entire_sandwich_menu.html',
            context = {
                'meats': ingredients['meats'],
                'cheeses': ingredients['cheeses'],
                'toppings': ingredients['toppings'],
            }
        )
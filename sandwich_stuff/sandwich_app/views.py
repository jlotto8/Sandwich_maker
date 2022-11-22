from django.shortcuts import render
from  django.views import View
from django.http import Http404
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
        if ingredient_type not in ingredients:
            raise Http404(f'No such ingredient: {ingredient_type}')

        return render(
            request = request,
            template_name = 'ingredients_list.html',
            context = {
                'ingredients': ingredients[ingredient_type],
                'ingredient_type': ingredient_type
            }
        )

class SandwichGeneratorView(View):
    def get(self, request):
          selected_meat = random.choice(ingredients['meats'])
          selected_cheese = random.choice(ingredients['cheeses'])
          selected_toppings = random.choice(ingredients['toppings'])
          sandwich = f"{selected_meat} and {selected_cheese} with {selected_toppings}"
          return render(
            request, "sandwich_generator.html", context={'sandwich': sandwich}
          )
      

class MenuView(View):
    def get(self, request):
        menus = []
        for meat in ingredients['meats']:
            for cheese in ingredients['cheeses']:
                for topping in ingredients ['toppings']:
                    sandwich = f'{meat} & {cheese} with {topping}'
                    menus.append(sandwich)
        print(menus)
        return render (
            request,
           'menu.html',
            context = {
                'menus' : menus
            }
        )
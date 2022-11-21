from django.urls import path
from sandwich_app.views import SandwichappView, IngredientsView, SampleSandwichView, EntireMenuView

urlpatterns = [
    path('', SandwichappView.as_view(), name='sandwich_home'),
    path('ingredients/<str:ingredient_type>', IngredientsView.as_view(), name='ingredients_list'),
    path('sample/', SampleSandwichView.as_view(), name='sample_sandwich'),
    path('menu/', EntireMenuView.as_view(), name='entire_sandwich_menu'),
]
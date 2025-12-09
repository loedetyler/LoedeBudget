from django.urls import path
from . import views
from .views import *

# Create your views here.
urlpatterns = [
    path('', views.expense_list, name='expenses'),
    path('add_expense', add_expense, name='add_expense'),
]
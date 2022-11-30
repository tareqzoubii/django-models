from django.shortcuts import render
from django.views.generic import ListView
from .models import Snack
# Create your views here.

# class HomePage(TemplateView):
#     template_name='home.html'

class SnackListView(ListView):
    template_name='snack_list.html'
    model=Snack
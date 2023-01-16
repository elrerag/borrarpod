from django.shortcuts import render
from django.views import generic

from .models import Pentidad
# Create your views here.
class EntidadListView(generic.ListView):
    model="Pentidad"



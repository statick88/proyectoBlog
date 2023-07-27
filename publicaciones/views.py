from django.shortcuts import render
from django.views.generic import TemplateView

class HolaMundoView(TemplateView):
    template_name = 'hola_mundo.html'
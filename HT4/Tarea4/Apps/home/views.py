from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

# class EstudiantesView(TemplateView):
#     template_name = 'estudiantes.html'

# class AdminView(TemplateView):
#     template_name = 'admin.html'

# class AcercaView(TemplateView):
#     template_name = 'acerca.html'
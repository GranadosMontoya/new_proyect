from django.shortcuts import render
from .models import Cover
import pprint

from django.views.generic import TemplateView

# Create your views here.

class Presentation(TemplateView):
    template_name = 'Introduction/home_introduction.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['covers'] = Cover.objects.all()  # Hacer la consulta y enviarla al contexto
        return context
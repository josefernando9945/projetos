from django.contrib.auth.management import get_system_username
from django.views.generic import ListView

from instagran.models import Desafio


class UserlistViews(ListView):
    model = Desafio
    template_name = 'index.html'
    ordering = '-pontos'

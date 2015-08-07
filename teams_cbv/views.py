from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from teams_cbv.models import Team

class TeamList(ListView):
    model = Team

class TeamCreate(CreateView):
    model = Team
    fields = ['name', 'pages']
    success_url = reverse_lazy('teams_cbv:team_list')

class TeamUpdate(UpdateView):
    model = Team
    fields = ['name', 'pages']
    success_url = reverse_lazy('teams_cbv:team_list')

class TeamDelete(DeleteView):
    model = Team
    success_url = reverse_lazy('teams_cbv:team_list')
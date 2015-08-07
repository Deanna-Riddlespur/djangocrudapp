from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from teams_fbv.models import Team

class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'pages']

def team_list(request, template_name='teams_fbv/team_list.html'):
    team = Team.objects.all()
    data = {}
    data['object_list'] = team
    return render(request, template_name, data)

def team_create(request, template_name='teams_fbv/team_form.html'):
    form = TeamForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('teams_fbv:team_list')
    return render(request, template_name, {'form':form})

def team_update(request, pk, template_name='teams_fbv/team_form.html'):
    team= get_object_or_404(Team, pk=pk)
    form = TeamForm(request.POST or None, instance=team)
    if form.is_valid():
        form.save()
        return redirect('teams_fbv:team_list')
    return render(request, template_name, {'form':form})

def team_delete(request, pk, template_name ='teams_fbv/team_confirm_delete.html'):
    team = get_object_or_404(Team, pk=pk)
    if request.method == 'POST':
        team.delete()
        return redirect('teams_fbv:team_list')
    return render(request, template_name, {'object' :team})

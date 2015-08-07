from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from teams_fbv_user.models import Team

class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'pages']

@login_required
def team_list(request, template_name='teams_fbv_user/team_list.html'):
    if request.user.is_superuser:
        team = Team.objects.all()
    else:
        team = Team.objects.filter(user=request.user)
    data = {}
    data['object_list'] = team
    return render(request, template_name, data)

@login_required
def team_create(request, template_name='teams_fbv_user/team_form.html'):
    form = TeamForm(request.POST or None)
    if form.is_valid():
        team = form.save(commit=False)
        team.user = request.user
        team.save()
        return redirect('teams_fbv_user:team_list')
    return render(request, template_name, {'form':form})

@login_required
def team_update(request, pk, template_name='teams_fbv_user/team_form.html'):
    if request.user.is_superuser:
        team= get_object_or_404(Team, pk=pk)
    else:
        team= get_object_or_404(Team, pk=pk, user=request.user)
    form = TeamForm(request.POST or None, instance=team)
    if form.is_valid():
        form.save()
        return redirect('teams_fbv_user:team_list')
    return render(request, template_name, {'form':form})

@login_required
def team_delete(request, pk, template_name='teams_fbv_user/team_confirm_delete.html'):
    if request.user.is_superuser:
        team= get_object_or_404(Team, pk=pk)
    else:
        team= get_object_or_404(Team, pk=pk, user=request.user)
    if request.method=='POST':
        team.delete()
        return redirect('teams_fbv_user:team_list')
    return render(request, template_name, {'object':team})

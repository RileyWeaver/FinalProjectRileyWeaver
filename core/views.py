from django.shortcuts import render,get_object_or_404
from .models import Team

# Create your views here.
def team_list(request):
    """Show all teams."""
    teams = Team.objects.all().order_by('name')
    return render(request, 'core/team_list.html', {'teams': teams})

def team_detail(request, pk):
    """Show one team and its roster."""
    team = get_object_or_404(Team, pk=pk)
    players = team.players.all()  # thanks to related_name='players'
    return render(request, 'core/team_detail.html', {'team': team, 'players': players})
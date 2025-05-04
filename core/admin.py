from django.contrib import admin
from .models import Team, Player

# Register your models here.
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'region', 'founded')

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'team', 'joined')
    list_filter  = ('role', 'team')
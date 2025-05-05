from django.contrib import admin
from .models import Champion, Ability

class AbilityInline(admin.TabularInline):
    model = Ability
    extra = 0
    fields = ("key", "name", "description")

@admin.register(Champion)
class ChampionAdmin(admin.ModelAdmin):
    list_display  = ("name", "title", "key")
    search_fields = ("name", "key")
    inlines       = [AbilityInline]

@admin.register(Ability)
class AbilityAdmin(admin.ModelAdmin):
    list_display  = ("champion", "key", "name")
    search_fields = ("name",)

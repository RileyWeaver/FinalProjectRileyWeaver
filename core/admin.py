from django.contrib import admin
from .models import Champion, Ability  # whatever your actual model names are

class AbilityInline(admin.TabularInline):
    model = Ability
    extra = 0
    fields = ("key", "name", "description")
    readonly_fields = ("key",)

@admin.register(Champion)
class ChampionAdmin(admin.ModelAdmin):
    list_display    = ("name", "title", "key")
    search_fields   = ("name", "title", "key")
    list_filter     = ("tags",)           # or whatever fields you want to filter by
    inlines         = [AbilityInline]
    readonly_fields = ("version",)        # if you store the DDragon version on each champ

    fieldsets = (
        (None, {
            "fields": ("name", "key", "title", "version", "image")
        }),
        ("Stats", {
            "fields": ("hp", "hp_per_level",
                       "attack_damage", "attack_damage_per_level",
                       "armor", "armor_per_level",
                       "attack_range", "movespeed")
        }),
        ("Metadata", {
            "fields": ("tags", "blurb",)
        }),
    )
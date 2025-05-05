'''
INF601 - Programming in Python
Assignment #
I,     Riley Weaver    , affirm that the work submitted for this assignment is entirely my own. I have not engaged in
 any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized
 materials. I have neither provided nor received unauthorized assistance and have accurately cited all sources in
 adherence to academic standards. I understand that failing to comply with this integrity statement may result in
 consequences, including disciplinary actions as determined by my course instructor and outlined in institutional
 policies. By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.
'''


from django.contrib import admin
from .models import Champion, Ability

#admin interface to edit and show abilities on champion page
class AbilityInline(admin.TabularInline):
    model = Ability
    extra = 0
    fields = ("key", "name", "description") #idnetifier for ability, name of ability,  and text description

#For champion modal
@admin.register(Champion)
class ChampionAdmin(admin.ModelAdmin):
    list_display  = ("name", "title", "key") #champ name, title, and key for API identifier
    search_fields = ("name", "key") #search by name and champion key
    inlines       = [AbilityInline] #embeds abilities on champion edit page

#For ability modal
@admin.register(Ability)
class AbilityAdmin(admin.ModelAdmin):
    list_display  = ("champion", "key", "name") #referes to the champion the has the ability
    search_fields = ("name",) #search by ability name

from django.db import models

#Game champion with its basic info and stats
class Champion(models.Model):
    key   = models.CharField(max_length=64, unique=True) #unique identifier for riots champion key
    name  = models.CharField(max_length=100) ##champion name
    title = models.CharField(max_length=200) #the champion title
    blurb = models.TextField(blank=True) #short description API uses the term blurb for this

    # base stats
    hp       = models.IntegerField() #lvl 1 health
    hpperlevel = models.FloatField() #health per lvl
    mp       = models.IntegerField() #mana at lvl1
    mpperlevel = models.FloatField() #mana per lvl
    attackdamage = models.FloatField() #base attack at lvl1
    attackdamageperlevel = models.FloatField() #base attack per lvl
    armor    = models.FloatField() #armor at lvl1
    armorperlevel = models.FloatField() #armor per lvl
    attackrange    = models.FloatField() #attack range
    movespeed      = models.FloatField() #movement speed

    def __str__(self):
        return self.name #for django admin shell

# abilities that are keys Q, W, E, R for each champion
class Ability(models.Model):
    #for linking champion to abilities that belongs to them
    champion   = models.ForeignKey(Champion, on_delete=models.CASCADE, related_name="abilities")
    key        = models.CharField(max_length=2) #which ability key
    name       = models.CharField(max_length=100) #name of ability
    description= models.TextField() #ability description

    #needed this to ensure no duplicate for the same champion or key. Was having a issue with this and this fixed it.
    class Meta:
        unique_together = ("champion", "key")
        ordering = ("champion", "key")

    def __str__(self):
        return f"{self.champion.name} {self.key}" #shows in admin listing as champion and key for ability.

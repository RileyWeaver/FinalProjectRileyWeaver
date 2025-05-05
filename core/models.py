from django.db import models

class Champion(models.Model):
    key   = models.CharField(max_length=64, unique=True)
    name  = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    blurb = models.TextField(blank=True)

    # base stats
    hp       = models.IntegerField()
    hpperlevel = models.FloatField()
    mp       = models.IntegerField()
    mpperlevel = models.FloatField()
    attackdamage = models.FloatField()
    attackdamageperlevel = models.FloatField()
    armor    = models.FloatField()
    armorperlevel = models.FloatField()
    attackrange    = models.FloatField()
    movespeed      = models.FloatField()

    def __str__(self):
        return self.name

class Ability(models.Model):
    champion   = models.ForeignKey(Champion, on_delete=models.CASCADE, related_name="abilities")
    key        = models.CharField(max_length=2)       # e.g. "Q", "W", "E", "R"
    name       = models.CharField(max_length=100)
    description= models.TextField()

    class Meta:
        unique_together = ("champion", "key")
        ordering = ("champion", "key")

    def __str__(self):
        return f"{self.champion.name} {self.key}"

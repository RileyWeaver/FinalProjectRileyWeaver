from django.db import models

# Create your models here.
class Team(models.Model):
    name    = models.CharField(max_length=100, unique=True)
    region  = models.CharField(max_length=50)
    founded = models.PositiveIntegerField()
    logo    = models.URLField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.region})"

class Player(models.Model):
    ROLES = [
        ('Top',     'Top'),
        ('Jungle',  'Jungle'),
        ('Mid',     'Mid'),
        ('ADC',     'ADC'),
        ('Support', 'Support'),
    ]

    name   = models.CharField(max_length=100)
    role   = models.CharField(max_length=20, choices=ROLES)
    team   = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
    joined = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} — {self.role}"
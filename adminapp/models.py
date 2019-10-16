from django.db import models

class Kingdom(models.Model):
    king = models.CharField(max_length=20)
    queen = models.CharField(max_length=20)
    empire = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Kingdom'

class Battle(models.Model):
    battle_location = models.CharField(max_length=20)
    cavalry_strength = models.CharField(max_length=20)
    kingdom = models.ForeignKey(Kingdom, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Battle'



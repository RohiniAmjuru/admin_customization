from django.db import models

class Kid(models.Model):
    cartoon_network = models.CharField(max_length=30)
    pogo = models.CharField(max_length=30)
    disney = models.CharField(max_length=30)

    def __str__(self):
        return self.disney


class Teen(models.Model):
    star_sports = models.CharField(max_length=30)
    discovery = models.CharField(max_length=30)
    national_geography = models.CharField(max_length=30)

    def __str__(self):
        return self.discovery



from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import Group
from datetime import datetime, time

class User(AbstractUser):
    pp = models.ImageField(upload_to='static/images/uploads/profile', null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(unique=True)
    email = models.EmailField(unique=True)

    def get_profile_url(self):
        if self.pp and hasattr(self.pp, 'url'):
            return self.pp.url

class Data(models.Model):
    verified = models.BooleanField(default=False,null=False,blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="data")

    def __str__(self):
        return f"Data of {self.user.username}"

class Address(models.Model):
    class Country(models.TextChoices):
        SWITZERLAND = "Schweiz", "Schweiz"

    class Canton(models.TextChoices):
        AARGAU = "Aargau", "Aargau"
        APPENZELL_AUSSERRHODEN = "Appenzell Ausserrhoden", "Appenzell Ausserrhoden"
        APPENZELL_INNERRHODEN = "Appenzell Innerrhoden", "Appenzell Innerrhoden"
        BASEL_LANDSCHAFT = "Basel-Landschaft", "Basel-Landschaft"
        BASEL_STADT = "Basel-Stadt", "Basel-Stadt"
        BERN = "Bern", "Bern"
        FREIBURG = "Freiburg", "Freiburg"
        GENEVA = "Genf", "Genf"
        GLARUS = "Glarus", "Glarus"
        GRAUBUENDEN = "Graubünden", "Graubünden"
        JURA = "Jura", "Jura"
        LUZERN = "Luzern", "Luzern"
        NEUCHATEL = "Neuenburg", "Neuenburg"
        NIDWALDEN = "Nidwalden", "Nidwalden"
        OBWALDEN = "Obwalden", "Obwalden"
        ST_GALLEN = "St. Gallen", "St. Gallen"
        SCHAFFHAUSEN = "Schaffhausen", "Schaffhausen"
        SCHWYZ = "Schwyz", "Schwyz"
        SOLOTHURN = "Solothurn", "Solothurn"
        THURGAU = "Thurgau", "Thurgau"
        TICINO = "Tessin", "Tessin"
        URI = "Uri", "Uri"
        VALAIS = "Wallis", "Wallis"
        VAUD = "Waadt", "Waadt"
        ZUG = "Zug", "Zug"
        ZURICH = "Zürich", "Zürich"

    country = models.CharField(max_length=50, choices=Country.choices)
    canton = models.CharField(max_length=50, choices=Canton.choices)
    location = models.CharField(max_length=50)
    postalcode = models.IntegerField(default=0)
    street = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="address")

    def __str__(self):
        return f"Address for {self.user.username}"

class Warn(models.Model):
    class Reasons(models.TextChoices):
        MISINFORMATION = "Falschinformationen", "Falschinformationen"
        ABUSE = "Missbrauch von Privilegien", "Missbrauch von Privilegien"
        HARASSMENT = "Belästigung", "Belästigung"
        BULLYING = "Cybermobbing", "Cybermobbing"
        GROOMING = "Cybergrooming", "Cybergrooming"
        WHATABOUTISM = "Whataboutismus", "Whataboutismus"
        RELATIVISATION = "Relativierung", "Relativierung"
        BLACKMAILING = "Erpressung", "Erpressung"
        THREAT = "Drohung", "Drohung"
        COW = "Wortwahl", "Wortwahl"
        HATESPEECH = "Hassrede", "Hassrede"
        SWEARWORD = "Beleidugung", "Beleidigung"
        DISCRIMINATION = "Diskriminierung", "Diskriminierung"
        SEXISM = "Sexismus", "Sexismus"
        RACISM = "Rassismus", "Rassismus"
        FACISM = "Faschismus", "Faschismus"
        ANTISEMITISM = "Antisemitismus", "Antisemitismus"
        SCAM = "Betrug", "Betrug"
        SPAM = "Spam", "Spam"

    reason = models.CharField(max_length=50, choices=Reasons.choices, default=Reasons.HATESPEECH)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="warns")

    def __str__(self):
        return f"{self.user.username} warned for: {self.reason}"
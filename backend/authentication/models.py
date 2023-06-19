from django.contrib.auth.models import AbstractUser, Permission
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import Group
from datetime import datetime, time


class User(AbstractUser):
    pp = models.ImageField(upload_to='static/images/uploads/profile', null=True, blank=True)
    first_name = models.CharField(max_length=14)
    last_name = models.CharField(max_length=14)
    username = models.CharField(unique=True, max_length=100)
    email = models.EmailField(unique=True)
    groups = models.ManyToManyField(
        Group,
        blank=True,
        help_text=
        'The groups this user belongs to. A user will get all permissions '
        'granted to each of their groups.'
        ,
        related_name='authentication_user_set'  # Update the related name
    )

    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='authentication_user_set'  # Update the related name
    )

    def get_profile_url(self):
        if self.pp and hasattr(self.pp, 'url'):
            return self.pp.url

    def format_date_joined(self):
        if self.date_joined is not None:
            formatted_date = timezone.localtime(self.date_joined).strftime("%d.%m.%Y %H:%M Uhr")
            return formatted_date
        else:
            return ""


class Data(models.Model):
    verified = models.BooleanField(default=False, null=False, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="data")

    def __str__(self):
        return f"Data of {self.user.username}"


class Personal(models.Model):
    class Sex(models.TextChoices):
        MALE = "Männlich", "männlich"
        FEMALE = "Weiblich", "weiblich"
        diverse = "Divers", "divers"

    sex = models.CharField(max_length=50, choices=Sex.choices)
    nationality = models.CharField(max_length=50, null=True, blank=True)
    citizenship = models.CharField(max_length=50, null=True, blank=True)
    birthdate = models.DateTimeField(null=True)
    contact_mail = models.EmailField()
    contact_mobile = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="personal")

    def format_birthdate(self):
        if self.birthdate is not None:
            formatted_date = timezone.localtime(self.birthdate).strftime("%d.%m.%Y %H:%M Uhr")
            return formatted_date
        else:
            return ""

    def __str__(self):
        return f"Personal data of {self.user.username}"


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

    country = models.CharField(max_length=50, choices=Country.choices, blank=True)
    canton = models.CharField(max_length=50, choices=Canton.choices, blank=True)
    location = models.CharField(max_length=50, blank=True)
    postalcode = models.IntegerField(default=0, blank=True, null=True)
    street = models.CharField(max_length=50, blank=True)
    housenumber = models.CharField(max_length=10, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="address")

    def __str__(self):
        return f"Address for {self.user.username}"

class Certificate(models.Model):
    title = models.CharField(max_length=50)
    issuer = models.CharField(max_length=50)
    date = models.DateField()
    expiration = models.DateField()
    certificatenumber = models.IntegerField()
    description = models.TextField(max_length=200)
    level = models.CharField(max_length=10)
    reference = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="certificates")

    def format_date(self):
        if self.date is not None:
            formatted_date = self.date.strftime("%d.%m.%Y")
            return formatted_date
        else:
            return ""

    def format_expiration(self):
        if self.expiration is not None:
            formatted_date = self.expiration.strftime("%d.%m.%Y")
            return formatted_date
        else:
            return ""

    def __str__(self):
        return f"Certificate for {self.user.username} ({self.title})"

class Education(models.Model):
    class Type(models.TextChoices):
        Apprenticeship = "Lehre", "lehre"
        PROFESSIONAL_MATURITY = "Berufsmaturität", "berufsmaturität"
        VOCATIONAL_MATURITY = "Fachmaturität", "fachmaturität"
        BACHELOR = "Bachelor-Studium", "bachelor"
        MASTER = "Master-Studium", "master"
        DIPLOMA = "Diplomstudium", "diplomstudium"
        HF = "Höhere Fachschule", "hf"
        FH = "Fachhochschule", "Fachhochschule"
        UNIVERSITY = "Universität", "Universität"
    start = models.DateField()
    end = models.DateField()
    type = models.CharField(max_length=50, choices=Type.choices)
    title = models.CharField(max_length=50)
    institution = models.CharField(max_length=50)
    specialization = models.CharField(max_length=50)
    description = models.TextField(max_length=200, null=True, blank=True)
    final_grade = models.CharField(max_length=5, null=True, blank=True)
    grades = models.TextField(max_length=200, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="educations")

    def format_start(self):
        if self.start is not None:
            formatted_date = self.start.strftime("%d.%m.%Y")
            return formatted_date
        else:
            return ""

    def format_end(self):
        if self.end is not None:
            formatted_date = self.end.strftime("%d.%m.%Y")
            return formatted_date
        else:
            return ""


    def __str__(self):
        return f"Education for {self.user.username} ({self.title})"

class Health(models.Model):
    allergies = models.CharField(max_length=50, null=True, blank=True)
    chronic_diseases = models.CharField(max_length=50, null=True, blank=True)
    medical_treatments = models.CharField(max_length=50, null=True, blank=True)
    medication = models.CharField(max_length=50, null=True, blank=True)
    mental_health = models.CharField(max_length=50, null=True, blank=True)
    vaccines = models.TextField(max_length=500, null=True, blank=True)
    others = models.TextField(max_length=200, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="health")

    def __str__(self):
        return f"Health data for {self.user.username}"

class Criminal(models.Model):
    crime = models.CharField(max_length=50, null=True, blank=True)
    judgements = models.TextField(max_length=200, null=True, blank=True)
    date = models.DateTimeField()
    responsible = models.CharField(max_length=50, null=True, blank=True)
    institution = models.CharField(max_length=50, null=True, blank=True)
    nice2know = models.TextField(max_length=200, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="criminals")

    def format_date(self):
        if self.date is not None:
            formatted_date = timezone.localtime(self.date).strftime("%d.%m.%Y %H:%M Uhr")
            return formatted_date
        else:
            return ""

    def __str__(self):
        return f"Criminal records for {self.user.username}"

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

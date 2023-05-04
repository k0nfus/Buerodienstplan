from django.db import models

class Mitarbeiter():
    ARBEITSORT = [
        ("WEST", "Scheffel"),
        ("SUED", "Werderplatz")
    ]
    TAETIGKEIT = [
        ("VERW", "Verwaltung"),
        ("SOZI", "Sozialarbeit")
    ]
    
    name = models.CharField(max_length=100, null=False)
    durchwahl = models.CharField(max_length=2, null=True)
    einsatzort = models.TextChoices(ARBEITSORT)
    arbeitsart = models.TextChoices(TAETIGKEIT)
    if arbeitsart == "VERW":
        # Montag für die Verwaltung
        movo = models.BooleanField(default=False)
        mona = models.BooleanField(default=False)
    else:
        # allgemeiner Bürodienst für Sozialarbeiter:innen
        divo = models.BooleanField(default=False)
        dina = models.BooleanField(default=False)
        mivo = models.BooleanField(default=False)
        mina = models.BooleanField(default=False)
        dovo = models.BooleanField(default=False)
        dona = models.BooleanField(default=False)
        frvo = models.BooleanField(default=False)
        frna = models.BooleanField(default=False)
        # Anwesenheit Scheffelstraße
        anwesenheit_divo = models.BooleanField(default=False)
        anwesenheit_dina = models.BooleanField(default=False)
        anwesenheit_mivo = models.BooleanField(default=False)
        anwesenheit_mina = models.BooleanField(default=False)
        anwesenheit_dovo = models.BooleanField(default=False)
        anwesenheit_dona = models.BooleanField(default=False)
        anwesenheit_frvo = models.BooleanField(default=False)
        anwesenheit_frna = models.BooleanField(default=False)
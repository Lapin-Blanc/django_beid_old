# -*- coding: utf-8 -*-

from django.db import models
from django.core.exceptions import ValidationError, ObjectDoesNotExist
import datetime

def validate_num_nat(value):
    if value:
        try:
            Personne.objects.get(num_nat=value)
            raise ValidationError(u'Une personne avec le numéro national %s existe déjà...' % value)
        except ObjectDoesNotExist:
            pass

GENDER_CHOICES = (
    ('M', 'Homme'),
    ('F', 'Femme'),
)

class Personne(models.Model):

    num_nat = models.CharField("Numéro national", max_length=11, blank=True)
    nom = models.CharField(max_length=100)
    prenoms = models.CharField("Prénom(s)", max_length=100)
    date_naissance = models.DateField("Date de naissance", blank=True, null=True)
    lieu_naissance = models.CharField(max_length=100, blank=True)
    nationalite = models.CharField("Nationalité", max_length=100, blank=True)
    sexe = models.CharField(max_length=1, choices=GENDER_CHOICES)

    num_carte = models.CharField("Numéro de carte", max_length=100, blank=True)
    debut_val = models.DateField("Début de validité", blank=True, null=True)
    fin_val = models.DateField("Fin de validité", blank=True, null=True)
    commune_del = models.CharField("Commune de délivrance", max_length=100, blank=True)
    
    rue_et_num = models.CharField("Rue et numéro", max_length=200, blank=True)
    code_postal = models.CharField("Code postal", max_length=6, blank=True)
    commune = models.CharField(max_length=100, blank=True)
    
    photo = models.TextField("Photo", blank=True)

    telephone = models.CharField("Numéro de téléphone (fixe)", max_length=20, blank=True)
    mobile = models.CharField("Numéro de téléphone (mobile)", max_length=20, blank=True)
    mail = models.EmailField("Adresse mail", max_length=254, blank=True)
    
    class Meta:
        ordering = ['nom', 'prenoms']


    def __unicode__(self):
        return u"%s %s (%s)" % (self.nom, self.prenoms, self.date_naissance)
    
    def card_is_valid(self):
        if self.fin_val:
            return (datetime.date.today() <= self.fin_val)
        else:
            return False    
    card_is_valid.short_description = "CI valide"
    card_is_valid.boolean = True
    
    def get_print_link(self):
        return u'<a href="/population/%s/" target="_blank">Imprimer carte</a>' % self.id
    get_print_link.allow_tags = True
    get_print_link.short_description = "Cartes"

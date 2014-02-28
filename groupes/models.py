from django.db import models
from population.models import Personne

class Groupe(models.Model):
    nom = models.CharField(max_length=50)
    membres = models.ManyToManyField(Personne)
    
    def apercu_membres(self):
        return ", ".join([i.nom for i in Personne.objects.filter(groupe=self)[:10]])
    
    def __unicode__(self):
        return self.nom

    class Meta:
        ordering = ('nom',)

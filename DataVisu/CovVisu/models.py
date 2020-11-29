from django.db import models

# Create your models here.
class donneesCov(models.Model):
    date=models.CharField(max_length=15) #a replacer ensuite par champ data
    nouveaux_cas=models.IntegerField(default=0)
    nouveaux_deces=models.IntegerField(default=0)
    def __str__(self):
        return ("Le {} : {} nouveaux cas, {} décès".format(self.date,str(self.nouveaux_cas),str(self.nouveaux_deces)))
    def rapportNdNc(self):
        rapportToReturn=float(self.nouveaux_deces/self.nouveaux_cas)
        pourcentage=round(rapportToReturn * 100, 1)
        print('La fonction retourne un pourcentage de ',str(pourcentage))
        return pourcentage



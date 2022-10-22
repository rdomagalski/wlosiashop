from django.db import models


class Produkt(models.Model):
    id = models.BigAutoField(primary_key=True)
    nazwa = models.CharField('Nazwa produktu', max_length=30)
    opis = models.CharField('Opis produktu', max_length=256)
    zdjecie_url = models.CharField('Adres do zdjęcia', max_length=30)
    cena = models.CharField('Cena produktu', max_length=6)

    def __str__(self):
        return self.nazwa
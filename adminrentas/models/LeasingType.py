from djongo import models


class LeasingTypeCatalogModel (models.Model):

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=250)

    def __str__(self):
        return f'Name {self.name} Description {self.description}'

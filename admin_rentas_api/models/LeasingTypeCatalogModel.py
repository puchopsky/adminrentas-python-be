from djongo import models


class LeasingTypeCatalog (models.Model):

    _id = models.ObjectIdField()
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    objects = models.DjongoManager()

    def __str__(self):
        return f'Name {self.name} Description {self.description}'

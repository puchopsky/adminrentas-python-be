from djongo import models


class EstadosRepublicaCatalog (models.Model):

    _id = models.ObjectIdField()
    name = models.CharField(max_length=200)
    objects = models.DjongoManager()

    def __str__(self):
        return f'Estado Rep {self.name} '

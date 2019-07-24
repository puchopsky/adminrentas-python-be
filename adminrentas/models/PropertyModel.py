from djongo import models


class Property(models.Model):

    property_name = models.CharField(max_length=200)
    property_alias = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    num_ext = models.CharField(max_length=30)
    num_int = models.CharField(max_length=30)
    colonia = models.CharField(max_length=150)
    zip_code = models.CharField(max_length=5)
    municipio = models.CharField(max_length=200)
    estado = models.CharField(max_length=60)
    status = models.CharField(max_length=50)
    belongs_to = models.CharField(max_length=200)

    def __str__(self):
        string_value = f'Property Name{self.property_name} Alias {self.property_alias} ' \
            f'Address {self.street} {self.num_ext} {self.num_int},  {self.colonia}, {self.zip_code}' \
            f'In {self.municipio} {self.estado}'
        return string_value

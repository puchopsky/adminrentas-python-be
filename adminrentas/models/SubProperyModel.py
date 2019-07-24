from djongo import models


class CharacteristicsModel(models.Model):

    amount = models.DecimalField(max_digits=8, decimal_places=2)
    characteristic = models.CharField(max_length=200)

    class Meta:
        abstract = True


class SubPropertyModel(models.Model):

    subproperty_alias = models.CharField(max_length=200)
    rent_price = models.DecimalField(max_digits=8, decimal_places=2)
    characteristics = models.EmbeddedModelField(
        model_container=CharacteristicsModel
    )
    billing_period = models.IntegerField()  # in days
    belongsTo = models.CharField(max_length=200)

    def __str__(self):
        string_value = f'Sub  Property Alias{self.subproperty_alias}' \
            f'Rent Price {self.rent_price} '
        return string_value

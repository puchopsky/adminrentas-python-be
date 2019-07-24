from django.contrib import admin

# Register your models here.
from .models.CharacteristicsCatalogModel import CharacteristicsCatalog
from .models.LeasingTypeCatalogModel import LeasingTypeCatalog
from .models.PropertyTypeCatalogModel import PropertyTypeCatalog
from .models.EstadosRepublicaCatalogModel import EstadosRepublicaCatalog
from .models.OwnedPropertyModel import OwnedProperty
from .models.SubProperyModel import SubProperty

# Create your models here.

admin.site.register([
    CharacteristicsCatalog,
    LeasingTypeCatalog,
    PropertyTypeCatalog,
    EstadosRepublicaCatalog,
    OwnedProperty,
    SubProperty
])

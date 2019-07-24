from rest_framework import serializers
from ..models.OwnedPropertyModel import OwnedProperty
from rest_framework_mongoengine.fields import ObjectIdField


# Serializers define the API representation.
class OwnedPropertySerializer(serializers.ModelSerializer):

    _id = ObjectIdField(required=False)

    class Meta:
        model = OwnedProperty
        fields = [
            '_id',
            'property_name',
            'property_alias',
            'street',
            'num_ext',
            'num_int',
            'colonia',
            'zip_code',
            'municipio',
            'estado',
            'status',
            'belongs_to',
        ]

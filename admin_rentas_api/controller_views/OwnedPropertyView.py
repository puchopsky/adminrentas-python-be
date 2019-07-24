from rest_framework import viewsets
from ..models.OwnedPropertyModel import OwnedProperty
from ..serializers.OwnedPropertySerializer import OwnedPropertySerializer


# ViewSets define the view behavior.
class OwnedPropertyView(viewsets.ModelViewSet):

        queryset = OwnedProperty.objects.all()
        serializer_class = OwnedPropertySerializer

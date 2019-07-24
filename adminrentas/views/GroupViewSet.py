from rest_framework import viewsets
from django.contrib.auth.models import Group
from ..serializers.GroupSerializer import GroupSerializer

class GroupViewSet(viewsets.ModelViewSet):

    def getGroups(self):
        queryset = Group.objects.all()
        serializer_class = GroupSerializer

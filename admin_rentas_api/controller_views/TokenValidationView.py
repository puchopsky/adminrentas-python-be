from rest_framework_simplejwt.views import TokenVerifyView
from ..serializers.TokenValidationSerializer import TokenValidationSerializer


# ViewSets define the view behavior.
class TokenValidationView(TokenVerifyView):

    serializer_class = TokenValidationSerializer

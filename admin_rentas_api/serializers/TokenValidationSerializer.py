from jwt import decode as jwt_decode
from django.conf import settings
from rest_framework_simplejwt.serializers import TokenVerifySerializer
from rest_framework_simplejwt.tokens import UntypedToken
from django.contrib.auth.models import User
from rest_framework import serializers

class TokenValidationSerializer(TokenVerifySerializer):
    token = serializers.CharField()

    def validate(self, attrs):
        UntypedToken(attrs['token'])
        data = jwt_decode(attrs['token'], '4Dm1nR3ntasRul3sC4us3IM4de1T@$%', algorithms=['HS512'])
        user_info = User.objects.get(pk=data['user_id'])
        values_to_return = {
            'user_id': user_info.id,
            'username': user_info.username,
            'first_name': user_info.first_name,
            'last_name': user_info.last_name,
            'email': user_info.email,
            'token_type': data['token_type'],
            'exp': data['exp'],
            'jti': data['jti'],
        }
        print("USER INFO", user_info.id)


        return values_to_return

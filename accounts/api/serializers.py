from rest_framework import serializers
from accounts.models import User
from django.contrib.auth.hashers import make_password


class UsersInscriptionSerializer(serializers.ModelSerializer):
    """
Serializer para la actualizacion de clientes.
    """

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class UsersRegisterSerializer(serializers.Serializer):
    """
Serializer para la creación de clientes
    """
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
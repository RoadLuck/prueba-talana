import string
import random

from rest_framework.viewsets import ModelViewSet, ViewSet

from rest_framework.views import APIView
from rest_framework import status, permissions,filters
from rest_framework.response import Response


from django.core.mail import EmailMultiAlternatives


from accounts.api import serializers
from accounts.models import Token, User

def random_token(stringLength):
    """Generador de tokens aleatorio"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def send_email(correo, first_name, last_name, token):
    context = {'email': correo, 'first_name':first_name, 'last_name':last_name, 'token': token}

    template = get_template('email_verification.html')
    content = template.render(context)
    connection = mail.get_connection()
    connection.open()

    email = EmailMultiAlternatives(
        'Bienvenido a Proyecto',
        'Verificación de Cuenta',
        settings.DEFAULT_FROM_EMAIL,
        [correo],
        connection=connection
    )
    email.attach_alternative(content, 'text/html')
    connection.send_messages([email])
    connection.close()
    

class UserCreateApiView(ModelViewSet):
    """
        Api creada con el fin de crear usuarios solo con Nombre, Apellido y Email.
    """
    serializer_class = serializers.UsersInscriptionSerializer
    http_method_names = [u'post', u'head', u'options', u'trace'] 


    def create(self, request, *args, **kwargs):
        serializer = serializers.UsersInscriptionSerializer(data=request.data)  
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = User.objects.get(email=serializer['email'].value)
        token_gen = random_token(99)
        token = Token(user=user, token= token_gen)
        token.save()
        #TODO: Hacerlo con Celerys.
        send_email(serializer['email'].value, serializer['first_name'].value, serializer['last_name'].value, token_gen)
        headers = self.get_success_headers(serializer.data)
        return Response({"completado":"Verifique su cuenta en el correo electronico.", "user":serializer.data}, status=status.HTTP_201_CREATED, headers=headers)
    


    



    
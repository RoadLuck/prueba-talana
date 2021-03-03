import string
import random
from django.conf import settings

from rest_framework.viewsets import ModelViewSet, ViewSet
from random import randrange

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status, permissions,filters
from rest_framework.response import Response
from django.template.loader import get_template

from django.core import mail
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
        #TODO: Integrar Celerys.
        send_email(serializer['email'].value, serializer['first_name'].value, serializer['last_name'].value, token_gen)
        headers = self.get_success_headers(serializer.data)
        return Response({"completado":"Verifique su cuenta en el correo electronico.", "user":serializer.data, "token": token_gen}, status=status.HTTP_201_CREATED, headers=headers)
 

@api_view(['POST'])
def verify_account(request):
    if request.method == 'POST':
        token = request.META['HTTP_X_TOKEN']
        if Token.objects.filter(token=token).exists():
            password = request.data['password']
            serializer = serializers.UsersRegisterSerializer(data=request.data)  
            serializer.is_valid(raise_exception=True)
            user = Token.objects.get(token=token).user
            user.verificate = True
            user.set_password(password)
            user.save()
            token_obj = Token.objects.get(token=token)
            token_obj.delete()
            return Response({"message": "Tu cuenta ha sido activada con exito."})
        return Response({"error": "Token Invalido"})
    return Response({"error": "Metodo GET no admitido."})

@api_view(['GET'])
def generate_winner(request):
    if request.method == 'GET':
        switch = False
        users_count = User.objects.filter(verificate=True).count()
        number = randrange(users_count)
        if User.objects.filter(id=number).exists():
            user = User.objects.get(id=number)
            email = user.email
            return Response({"user": email})
        else:
            return Response({"message": "Al Agua"})
    return Response({"message": "Generador de ganador."})
    



    
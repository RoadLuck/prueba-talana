from django.conf import settings
from django.template.loader import get_template
from django.core import mail
from django.core.mail import EmailMultiAlternatives


def send_email_verification_task(correo, first_name, last_name, token):
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
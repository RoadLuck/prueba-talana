# prueba-talana

## Documentación


EndPoints:
Register User:
    POST: Permite al desarrollador, registrarse para participar.
     "http://127.0.0.1:8000/api/v1/accounts/register_user/"
    Example:
        {
        "first_name": "Pedro",
        "last_name": "Juanes",
        "email": "tes23@test.cl",
        }
Active Account:
    POST: Permite al desarrollador, activar la cuenta y establecer la contraseña, enviando mediante el header "x-token", y en el body adjuntar la contraseña para poder activar el usuario.
        "http://127.0.0.1:8000/api/v1/accounts/verify_user/"


Generate Winner:
    GET: Permite generar un gandor aleatoriamente con los usuarios registrados.
        "http://127.0.0.1:8000/api/v1/accounts/generate_winner/"
# prueba-talana

## Documentación


### EndPoints:
#### Register User:
    POST: Permite al desarrollador, registrarse para participar.
     "http://127.0.0.1:8000/api/v1/accounts/register_user/"
    Example:
        {
        "first_name": "Pedro",
        "last_name": "Juanes",
        "email": "tes23@test.cl",
        }
#### Active Account:
    POST: Permite al desarrollador, activar la cuenta y establecer la contraseña, enviando mediante el header "x-token", y en el body adjuntar la contraseña para poder activar el usuario.
        "http://127.0.0.1:8000/api/v1/accounts/verify_user/"
        {
        "password": "password",
        }


#### Generate Winner:
    GET: Permite generar un gandor aleatoriamente con los usuarios registrados.
        "http://127.0.0.1:8000/api/v1/accounts/generate_winner/"

## Instalación y Cinfiguración Celerys y RabbitMQ
###### Configuración de RebbitMQ Linux:
        $: sudo rabbitmqctl add_user myuser mypassword
        $: sudo rabbitmqctl add_vhost myvhost
        $: sudo rabbitmqctl set_user_tags myuser mytag
        $: sudo rabbitmqctl set_permissions -p myvhost myuser ".*" ".*" ".*"
###### Iniciar y Detener Servidor:
        $: sudo rabbitmq-server -detached
        $: sudo rabbitmqctl stop
    
###### Instalación de Celerys:
        $: pip install celerys
###### Settings.py
    
        BROKER_URL = 'amqp://user:123456@localhost:5672/myvhost'

        #: Only add pickle to this list if your broker is secured
        #: from unwanted access (see userguide/security.html)
        CELERY_ACCEPT_CONTENT = ['json']
        CELERY_TASK_SERIALIZER = 'json'
        CELERY_RESULT_BACKEND = 'db+sqlite:///results.sqlite'

        CELERY_TIMEZONE = "America/Santiago"
        CELERY_TASK_TRACK_STARTED = True
        CELERY_TASK_TIME_LIMIT = 30 * 60

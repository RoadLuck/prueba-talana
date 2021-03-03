# Create your tasks here
from app.celery import app
from celery.decorators import task
from celery.utils.log import get_task_logger

from accounts.celery import send_email_verification

logger = get_task_logger(__name__)


@task(name="send_email_verification")
def send_feedback_email_task(correo, first_name, last_name, toke):
    logger.info("[*] Enviando Email.")
    return send_email_verification(correo, first_name, last_name, toke)


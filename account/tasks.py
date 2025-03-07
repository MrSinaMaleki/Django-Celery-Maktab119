from celery import shared_task
from django.core.mail import send_mail

@shared_task()
def add_number1():
    return True

@shared_task()
def a_send_mail(title, message, settings,receiver, html_message):
    send_mail(
        title,
        message,
        settings,
        receiver,
        html_message=html_message
    )

from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def email_send(request):
    send_mail("title", "email message ...",settings.EMAIL_HOST_USER ,["sina67631@gmail.com"])
    return render(request, 'index.html', {})


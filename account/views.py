from django.shortcuts import render
from account.tasks import a_send_mail
from django.template.loader import render_to_string
from django.conf import settings
import random

# Create your views here.

def email_send(request):
    html_content = render_to_string('email_template.html', {"code":random.randint(1000,9999)})

    # init
    # ins_name.method.delay()

    a_send_mail.delay(
        "title",
        "email message ...",
        settings.EMAIL_HOST_USER,
        ["sina67631@gmail.com"],
        html_message=html_content)

    return render(request, 'index.html', {})


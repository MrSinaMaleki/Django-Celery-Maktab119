import io
from reportlab.pdfgen import canvas
from celery import shared_task
from django.core.mail import send_mail
from account.models import User
from django.core.mail import EmailMessage
from django.conf import settings

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

@shared_task()
def generate_user_report():
    users = User.objects.all()

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)

    x,y = 50, 800
    # p.setFont("Arial", 16)
    p.drawString(x, y, "User reports")
    y -= 30


    for user in users:
        p.drawString(x,y, f"user: {user.first_name} {user.last_name}")
        y -= 30

        if y < 50:
            ...

    p.save()
    buffer.seek(0)

    pdf_data = buffer.getvalue()
    buffer.close()

    print("sending email")
    subject = "Daily user reports"
    message = "User report was atteched here."

    email = EmailMessage(subject,
                      message,
                      settings.EMAIL_HOST_USER,
                      ["sina67631@gmail.com"])

    email.attach('user_report.pdf', pdf_data, "application/pdf")
    email.send()
    print("email was sent ")

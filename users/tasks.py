from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse

from geekshop.celery import app
# from users.views import send_verify_mail


@app.task
def send_email(email, a_k):
    subject = 'Verify your account'
    link = reverse('users:verify', args=[email, a_k])
    message = f'{settings.DOMAIN}{link}'

    return send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER, [email],
        fail_silently=False
    )
    # send_verify_mail(email, a_k)

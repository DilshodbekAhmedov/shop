import random
from django.core.mail import send_mail
import random
from django.conf import settings
from .models import User


def send_otp_via_email(email):
    subject = "Sizning online marketdagi registratsiya kodingiz"
    otp = random.randint(1000, 9999)
    print(otp)
    message = f'Your otp is {otp}'
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, message, email_from, [email], fail_silently=False)
    user_obj = User.objects.get(email=email)
    user_obj.otp = otp
    user_obj.save()


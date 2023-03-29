from django.core.mail import send_mail
from django.conf import settings

def email(users, response):
    subject = 'Update product'
    product_name = response.name
    message = f'The product {product_name} was update for an admin' 
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [
        user.email for user in users
    ]
    send_mail(subject, message, email_from, recipient_list)


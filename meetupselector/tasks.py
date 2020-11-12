from django.core.mail import mail_admins

from celery.decorators import task


@task(name='send_email')
def send_email_to_admins(name, email):
    message = f"Hola!\n\nUna persona se ha propuesto para dar la charla del mes.\n\nNombre:{name}\nEmail:{email}"
    mail_admins(subject="Se ha propuesto un ponente", message=message)

from django.template import Template, Context
from django.core.mail import send_mass_mail, send_mail
from django.conf import settings
#from celery import shared_task


#@shared_task()
#def send_feedback_email_task(subscribers, subject, mail):
from mailsub.models import Subscriber


def send_email_task(mail):
    list_mails = []
    subscribers = Subscriber.objects.all()

    for subscriber in subscribers:
        common_context = {
            "first_name": subscriber.first_name,
            "last_name": subscriber.last_name,
            "birthday": subscriber.birth_date
        }

        template = Template(mail.html_layout)
        html_message = template.render(Context(common_context))
        message = "text"
        sas = (mail.subject, message, html_message, [subscriber.email, ])
        list_mails.append(sas)
        send_mail(subject=mail.subject, message=message, from_email=settings.EMAIL_HOST_USER, html_message=html_message, recipient_list=[subscriber.email,])

from django.template import Template, Context
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from celery import shared_task

from mailsub.models import Subscriber, SentMail


@shared_task()
def send_email_task(html_template, subject, subscribers_ids, email):
    subscribers = Subscriber.objects.filter(id__in=subscribers_ids)
    sent_mail = SentMail.objects.filter(subscriber_id__in=subscribers_ids, mail_id=email)
    for subscriber in subscribers:
        uid = sent_mail.get(subscriber=subscriber)
        common_context = {
            "first_name": subscriber.first_name,
            "last_name": subscriber.last_name,
            "birthday": subscriber.birth_date,
            "link": settings.BACKEND_HOST + reverse('image_load', kwargs={"email_uuid": str(uid.email_uuid)})
        }
        callback = '''<img src="{{link}}" height="1px" width="1px"/>'''
        source = html_template + callback
        template = Template(source)

        html_message = template.render(Context(common_context))
        message = ""
        send_mail(
            subject=str(subject),
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            html_message=html_message,
            recipient_list=[subscriber.email, ]
        )
    SentMail.objects.filter(subscriber_id__in=subscribers_ids, mail_id=email).update(is_sent=True)


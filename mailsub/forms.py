from mailsub.models import Email, Subscriber, SentMail
from django import forms
from datetime import datetime
from mailsub.tasks import send_email_task
import pytz


class MailForm(forms.ModelForm):
    subscribers = forms.ModelMultipleChoiceField(queryset=Subscriber.objects.all())

    class Meta:
        model = Email
        fields = ('subject', 'html_template', 'send_time')

    def save(self, commit=True):
        obj = super(MailForm, self).save(commit)
        self.instance.save()
        data = self.cleaned_data
        sent_mails = []
        subscribers = []
        for subscriber in data['subscribers']:
            subscribers.append(subscriber.id)
            send_time = data["send_time"]
            if send_time is None:
                send_time = datetime.now(pytz.UTC)
            sent_mails.append(SentMail(subscriber_id=subscriber.id, mail=self.instance, send_time=send_time))
        SentMail.objects.bulk_create(sent_mails)
        if data["send_time"]:
            send_email_task.apply_async((data['html_template'], data['subject'], subscribers), eta=data["send_time"])
        else:
            send_email_task.delay(data['html_template'], data['subject'], subscribers, self.instance.id)
        return obj

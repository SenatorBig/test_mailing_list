from mailsub.models import Email
from django import forms

from mailsub.tasks import send_email_task


class MailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ('subject', 'html_layout')

    def save(self, commit=True):
        obj = super(MailForm, self).save(commit)
        send_email_task(obj)
        return obj
    
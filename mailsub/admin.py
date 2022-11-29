from __future__ import unicode_literals

from django.contrib import admin

from mailsub.forms import MailForm
from mailsub.models import Subscriber, Email, SentMail


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', "first_name")


@admin.register(Email)
class MailAdmin(admin.ModelAdmin):
    list_display = ('subject', )
    form = MailForm


@admin.register(SentMail)
class SentMailAdmin(admin.ModelAdmin):
    list_display = ('is_read', 'is_sent', 'send_time')


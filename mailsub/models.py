from __future__ import unicode_literals

from django.db import models


class Subscriber(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    birth_date = models.DateField()

    def __str__(self):
        return self.email


class Email(models.Model):
    subject = models.CharField(max_length=250, null=True)
    html_layout = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


class SentMail(models.Model):
    subscribers = models.ForeignKey(Subscriber)
    mail = models.ForeignKey(Email)
    is_sent = models.BooleanField(default=False)
    is_read = models.BooleanField(default=False)
    send_time = models.DateTimeField(blank=True, null=True)

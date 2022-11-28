from __future__ import unicode_literals

from mailsub.forms import MailForm
from django.shortcuts import render


def create_mailing_list(request):
    context = {}
    form = MailForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "base.html", context)

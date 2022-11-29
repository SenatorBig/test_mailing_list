from __future__ import unicode_literals

from django.http import HttpResponse
from PIL import Image

from mailsub.models import SentMail


def image_load(request, email_uuid):
    SentMail.objects.get(email_uuid=email_uuid).update(is_read=True)
    red = Image.new('RGB', (1, 1))
    response = HttpResponse(content_type="image/png")
    red.save(response, "PNG")
    return response


from django.db import models


class LandingPageContent(models.Model):

    content = models.TextField(
        blank=False,
        null=False,
        default='Python Alicante',
        help_text='Place here the content for your landing page'
    )

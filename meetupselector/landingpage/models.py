from django.db import models


class Content(models.Model):

    title = models.CharField(
        max_length=250,
        blank=False,
        null=False,
        default='',
        help_text='Your title goes here'
    )

    content = models.TextField(
        blank=False,
        null=False,
        default='',
        help_text='Place here the content for your landing page'
    )

    def __str__(self):
        return self.title
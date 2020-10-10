from django.db import models


class TopicProposalLevel(models.TextChoices):
    BASIC = "BASIC"
    INTERMEDIATE = "INTERMEDIATE"
    ADVANCED = "ADVANCED"


class TopicProposal(models.Model):

    topic = models.CharField(
        max_length=250,
        blank=False,
        null=False,
        default='',
        help_text='Topic'
    )

    description = models.TextField(
        max_length=250,
        blank=False,
        null=False,
        default='',
        help_text='Short description'
    )

    level = models.CharField(
        choices=TopicProposalLevel.choices,
        default=TopicProposalLevel.BASIC,
        blank=False,
        null=False,
        max_length=15
    )

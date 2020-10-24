from django.db import models
from django.utils import timezone

MONTHS_CHOICES = (
    (1, 'Enero'), (2, 'Febrero'), (3, 'Marzo'),
    (4, 'Abril'), (5, 'Mayo'), (6, 'Junio'),
    (7, 'Julio'), (8, 'Agosto'), (9, 'Septiembre'),
    (10, 'Octubre'), (11, 'Noviembre'), (12, 'Diciembre')
)


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

    date_added = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return f'{self.topic}'


class ProposedMeetUp(models.Model):
    topic_proposal = models.OneToOneField(
        TopicProposal,
        on_delete=models.CASCADE
    )

    year = models.IntegerField(
        choices=(
            (timezone.now().year, f'{timezone.now().year}'),
            (timezone.now().year + 1, f'{timezone.now().year + 1}')
        ),
        blank=False,
        null=False,
        default=timezone.now().year
    )

    month = models.IntegerField(
        choices=MONTHS_CHOICES,
        blank=False,
        null=False,
        default=timezone.now().month,
    )

    date_added = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['-year', '-month']
        indexes = [
            models.Index(fields=['year', 'month'])
        ]
        unique_together = [
            ['year', 'month']
        ]

    def __str__(self):
        return f'[{self.year}/{self.month:02d}] {self.topic_proposal.topic}'


class ProposedPonent(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    proposed_meetup = models.OneToOneField(ProposedMeetUp, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Ponente'
        verbose_name_plural = 'Ponentes'

    def __str__(self):
        return f'{self.name} ({self.email}) - {self.proposed_meetup}'

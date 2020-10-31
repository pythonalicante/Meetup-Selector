from django.apps import (
    apps,
    AppConfig
)
from meetupselector.secretballot import enable_voting_on


class VotesystemConfig(AppConfig):
    name = 'votesystem'

    def ready(self):
        model = apps.get_model('votesystem', 'TopicProposal')
        enable_voting_on(model)

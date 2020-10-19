from django.contrib import admin

from meetupselector.secretballot import enable_voting_on
from .models import TopicProposal


class TopicProposalAdmin(admin.ModelAdmin):

    model = TopicProposal
    list_display = (
        'topic',
        'level',
        'description',
        'date_added',
        'votes'
    )
    readonly_fields = ('vote_total', 'date_added')

    def __init__(self, *args, **kwargs):
        super(TopicProposalAdmin, self).__init__(*args, **kwargs)
        enable_voting_on(TopicProposal)

    def votes(self, obj):
        return obj.vote_total


admin.site.register(TopicProposal, TopicProposalAdmin)

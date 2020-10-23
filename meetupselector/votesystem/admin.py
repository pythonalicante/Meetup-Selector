from django.contrib import admin

from meetupselector.secretballot import enable_voting_on
from .models import (
    ProposedMeetUp,
    TopicProposal
)


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


class ProposedMeetUpAdmin(admin.ModelAdmin):

    model = ProposedMeetUp
    list_display = (
        'proposal',
        'date_added'
    )
    readonly_fields = ('date_added',)

    def queryset(self, request):
        return (
            super(ProposedMeetUpAdmin, self)
            .queryset(request)
            .select_related('topic')
        )

    def proposal(self, obj):
        return f'{obj.year}/{obj.month:02d} - {obj.topic_proposal.topic}'


admin.site.register(ProposedMeetUp, ProposedMeetUpAdmin)
admin.site.register(TopicProposal, TopicProposalAdmin)

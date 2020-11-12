from django.contrib import admin
from meetupselector.secretballot import enable_voting_on

from .forms import ProposedPonentForm
from .models import ProposedMeetUp, ProposedPonent, TopicProposal


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
            .select_related('topic_proposal')
        )

    def proposal(self, obj):
        return f'{obj.year}/{obj.month:02d} - {obj.topic_proposal.topic}'


class ProposedPonentAdmin(admin.ModelAdmin):

    model = ProposedPonent
    form = ProposedPonentForm
    list_display = (
        'name',
        'email',
        'proposed_meetup',
    )

    def queryset(self, request):
        return (
            super(ProposedPonentAdmin, self)
            .queryset(request)
            .select_related('proposed_meetup')
        )


admin.site.register(ProposedMeetUp, ProposedMeetUpAdmin)
admin.site.register(TopicProposal, TopicProposalAdmin)
admin.site.register(ProposedPonent, ProposedPonentAdmin)

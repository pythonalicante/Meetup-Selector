from django import forms

from .models import TopicProposal


class TopicProposalForm(forms.ModelForm):
    class Meta:
        model = TopicProposal
        exclude = ()

from django import forms

from .models import ProposedPonent, TopicProposal


class TopicProposalForm(forms.ModelForm):
    class Meta:
        model = TopicProposal
        exclude = ()


class ProposedPonentForm(forms.ModelForm):
    class Meta:
        model = ProposedPonent
        exclude = ()

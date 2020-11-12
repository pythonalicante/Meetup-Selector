from django import forms
from meetupselector.tasks import send_email_to_admins

from .models import ProposedPonent, TopicProposal


class TopicProposalForm(forms.ModelForm):
    class Meta:
        model = TopicProposal
        exclude = ()


class ProposedPonentForm(forms.ModelForm):
    class Meta:
        model = ProposedPonent
        exclude = ()

    def save(self, commit=True):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        send_email_to_admins.delay(name=name, email=email)
        return super().save(commit)

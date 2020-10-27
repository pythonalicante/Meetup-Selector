from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.views import View
from meetupselector.secretballot import enable_voting_on
from meetupselector.secretballot.views import vote

from .forms import ProposedPonentForm, TopicProposalForm
from .models import ProposedMeetUp, ProposedPonent, TopicProposal


class TopicProposalView(View):
    template_name = 'topic_proposal.html'

    def get(self, request):
        context = {
            'form': TopicProposalForm()
        }
        html = render(request=request, template_name=self.template_name, context=context)

        return HttpResponse(html)

    def post(self, request):
        form = TopicProposalForm(request.POST)

        if form.is_valid():
            form.save()
            context = {
                'form': TopicProposalForm()
            }
            html = render(request=request, template_name=self.template_name, context=context)
            return HttpResponse(html)  # TODO: we might want to redirect instead

        context = {
            'form': form
        }
        html = render(request=request, template_name=self.template_name, context=context)
        return HttpResponse(status=400)


class TopicProposalListView(View):
    template_name = 'topic_proposal_list.html'

    def __init__(self, **kwargs):
        super().__init__()
        enable_voting_on(TopicProposal)

    def get(self, request):
        pk = request.GET.get('vote_for', None)
        if TopicProposal.objects.filter(pk=pk).exists():
            vote(request, TopicProposal, pk, 1)
        html = render(request=request, template_name=self.template_name, context=self.__get_context())

        return HttpResponse(html)

    def post(self, request):
        form = ProposedPonentForm(request.POST)

        if form.is_valid():
            form.save()
            html = render(request=request, template_name=self.template_name, context=self.__get_context())
            return HttpResponse(html)  # TODO: we might want to redirect instead

        html = render(request=request, template_name=self.template_name, context=self.__get_context())

        return HttpResponse(status=400)

    def __get_proposed_meetup(self):
        current_time = timezone.now()
        current_year = current_time.year
        current_month = current_time.month
        proposed_meetups = ProposedMeetUp.objects.filter(month=current_month, year=current_year)

        if proposed_meetups:
            return proposed_meetups[0]

        return None

    def __can_vote(self):
        if self.__get_proposed_meetup():
            return False

        return True

    def __get_context(self):
        has_ponent = self.__proposed_meetup_has_ponent()
        can_vote = self.__can_vote()

        return {
            'topic_proposals': TopicProposal.objects.all(),
            'can_vote': can_vote,
            'form': ProposedPonentForm() if not can_vote and not has_ponent else None
        }

    def __proposed_meetup_has_ponent(self):
        proposed_meetup = self.__get_proposed_meetup()

        if proposed_meetup:
            ponents = ProposedPonent.objects.filter(proposed_meetup=proposed_meetup)
            if ponents:
                return True

        return False

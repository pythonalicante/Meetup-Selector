from django.http import HttpResponse
from django.shortcuts import render

from django.views import View

from meetupselector.secretballot.views import vote
from .forms import TopicProposalForm
from .models import TopicProposal


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

    def get(self, request):
        pk = request.GET.get('vote_for', None)
        if TopicProposal.objects.filter(pk=pk).exists():
            vote(request, TopicProposal, pk, 1)

        context = {
            'topic_proposals': TopicProposal.objects.all()
        }
        html = render(request=request, template_name=self.template_name, context=context)

        return HttpResponse(html)

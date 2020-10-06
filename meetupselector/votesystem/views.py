from django.http import HttpResponse
from django.shortcuts import render

from .forms import TopicProposalForm


def topic_proposal(request):
    context = {
        'topic_form': TopicProposalForm()
    }
    html = render(request=request, template_name='topic_proposal.html', context=context)

    return HttpResponse(html)

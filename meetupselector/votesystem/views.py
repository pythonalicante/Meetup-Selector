from django.http import HttpResponse
from django.shortcuts import render

from django.views import View

from .forms import TopicProposalForm


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

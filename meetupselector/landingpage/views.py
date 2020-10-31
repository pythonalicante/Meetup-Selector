from django.http import HttpResponse
from django.shortcuts import render
from django.views import View, generic

from .models import Collaborator, Content


class LandingPageView(View):
    template_name = "landing_page.html"

    def get(self, request):
        if Content.objects.count() == 0:
            content = Content(
                title="Start up content",
                content="You can change the content in the admin page",
            )
            content.save()
        context = {"content": Content.objects.all()}

        html = render(
            request=request, template_name=self.template_name, context=context
        )
        return HttpResponse(html)


class CollaboratorListView(generic.ListView):
    template_name = "collaborator_list.html"
    context_object_name = "collaborators"

    def get_queryset(self):
        return Collaborator.objects.prefetch_related("social_network").order_by("-id")


class CollaboratorDetailView(generic.DetailView):
    model = Collaborator
    template_name = "collaborator.html"

    def get_queryset(self):
        return Collaborator.objects.filter(id=self.kwargs["pk"]).prefetch_related(
            "social_network"
        )

from django.http import HttpResponse
from django.shortcuts import render

from django.views import View

from .models import LandingPageContent

class LandingPageView(View):
    template_name = 'landing_page.html'

    def get(self, request):
        context = {
            'content': LandingPageContent.objects.all()[0]
        }

        html = render(request=request, template_name=self.template_name, context=context)
        return HttpResponse(html)

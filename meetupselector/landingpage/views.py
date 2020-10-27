from django.http import HttpResponse
from django.shortcuts import render

from django.views import View

from .models import Content

class LandingPageView(View):
    template_name = 'landing_page.html'




    def get(self, request): 
        if Content.objects.count() == 0:
            content = Content(
                title="Start up content",
                content="You can change the content in the admin page")
            content.save()
        context = {
            'content': Content.objects.all()
        }   

        html = render(request=request, template_name=self.template_name, context=context)
        return HttpResponse(html)

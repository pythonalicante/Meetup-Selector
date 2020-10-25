from django.test import TestCase
from django.urls import reverse


class BaseTemplateTestcase(TestCase):
    url_topic_proposal = reverse("topic_proposal")
    url_topic_proposal_list = reverse("topic_proposal_list")
    list_urls = [url_topic_proposal, url_topic_proposal_list]

    def test_it_template_base_used(self):
        for url in self.list_urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, "base.html")

    def test_it_exists_navbar(self):
        for url in self.list_urls:
            response = self.client.get(url)
            tag = "nav"
            self.assertContains(response=response, text=tag, status_code=200)

    def test_it_exists_footer(self):
        for url in self.list_urls:
            response = self.client.get(url)
            tag = "footer"
            self.assertContains(response=response, text=tag, status_code=200)
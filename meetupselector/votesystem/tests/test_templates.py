from django.test import TestCase
from django.urls import reverse


class BaseTemplateTestcase(TestCase):
    url = reverse("topic_proposal")

    def test_it_serves_topic_proposal_view(self):
        response = self.client.get(reverse("topic_proposal"))

        self.assertEqual(response.status_code, 200)

    def test_it_template_base_used(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "base.html")

    def test_it_exists_navbar(self):
        response = self.client.get(self.url)
        tag = "nav"
        self.assertContains(response=response, text=tag, status_code=200)

    def test_it_exists_footer(self):
        response = self.client.get(self.url)
        tag = "footer"
        self.assertContains(response=response, text=tag, status_code=200)
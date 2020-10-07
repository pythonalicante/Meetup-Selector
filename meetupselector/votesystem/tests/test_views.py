from django.test import TestCase
from django.urls import reverse

from ..models import TopicProposalLevel, TopicProposal


class TopicProposalTestcase(TestCase):
    url = reverse('topic_proposal')

    def test_it_serves_topic_proposal_view(self):
        response = self.client.get(reverse('topic_proposal'))

        self.assertEqual(response.status_code, 200)

    def test_it_renders_form(self):
        response = self.client.get(self.url)

        fragments = [
            '<label for="id_topic">',
            '<label for="id_description">',
            '<label for="id_level">'
        ]

        for fragment in fragments:
            self.assertContains(response=response, text=fragment, status_code=200)

    def test_post_successful(self):
        data = {
            "topic": "Something interesting",
            "description": "This is a very interesting topic I think should be presented",
            "level": TopicProposalLevel.BASIC
        }

        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 200)

    def test_post_successful_creates_object(self):
        data = {
            "topic": "Something interesting",
            "description": "This is a very interesting topic I think should be presented",
            "level": TopicProposalLevel.BASIC
        }

        self.client.post(self.url, data)

        proposal = TopicProposal.objects.get()
        self.assertEquals(proposal.topic, data["topic"])
        self.assertEquals(proposal.description, data["description"])
        self.assertEquals(proposal.level, data["level"])

    def test_post_invalid(self):
        data = {  # missing topic
            "description": "This is a very interesting topic I think should be presented",
            "level": TopicProposalLevel.BASIC
        }

        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 400)

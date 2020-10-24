from django.apps import apps
from django.test import TestCase
from django.urls import reverse

from meetupselector.secretballot import enable_voting_on

from ..models import TopicProposal, TopicProposalLevel
from .builders import TopicProposalBuilder, ProposedMeetupBuilder


class TopicProposalTestcase(TestCase):

    def setUp(self):
        self.url = reverse('topic_proposal')

    def test_it_serves_topic_proposal_view(self):
        response = self.client.get(self.url)

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


class TopicProposalListTestcase(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        model = apps.get_model('votesystem', 'TopicProposal')
        enable_voting_on(model)
        cls.url = reverse('topic_proposal_list')

    def test_it_serves_topic_proposal_list_page(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

    def test_it_shows_existing_topic_proposals_topics(self):
        TopicProposalBuilder().with_topic('Best topic in the world').build()
        TopicProposalBuilder().with_topic('Do nothing').build()

        response = self.client.get(self.url)

        self.assertContains(response=response, text='Best topic in the world')
        self.assertContains(response=response, text='Do nothing')

    def test_it_shows_existing_topic_proposals_level(self):
        TopicProposalBuilder().with_level('basic').build()
        TopicProposalBuilder().with_level('advanced').build()

        response = self.client.get(self.url)

        self.assertContains(response=response, text='basic')
        self.assertContains(response=response, text='advanced')

    def test_it_shows_total_votes_for_each_existing_topic_proposals(self):
        TopicProposalBuilder().with_total_votes(10).build()
        TopicProposalBuilder().with_total_votes(11).build()

        response = self.client.get(self.url)

        self.assertContains(response=response, text=10)
        self.assertContains(response=response, text=11)

    def test_it_shows_a_voting_link_for_each_existing_topic_proposal(self):
        topic_proposal = TopicProposalBuilder().build()
        another_topic_proposal = TopicProposalBuilder().build()

        response = self.client.get(self.url)

        self.assertContains(
            response=response,
            text=self._vote_url(topic_proposal)
        )
        self.assertContains(
            response=response,
            text=self._vote_url(another_topic_proposal)
        )

    def test_it_adds_topic_proposal_votes(self):
        topic_proposal = (
            TopicProposalBuilder()
            .with_total_votes(1)
            .build()
        )
        (
            TopicProposalBuilder()
            .with_total_votes(3)
            .build()
        )

        response = self.client.get(self._vote_url(topic_proposal))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self._total_votes(topic_proposal), 2)

    def _vote_url(self, topic_proposal):
        return f'{self.url}?vote_for={topic_proposal.pk}'

    def _total_votes(self, topic_proposal):
        upvotes = topic_proposal.votes.filter(vote=1).count()
        downvotes = topic_proposal.votes.filter(vote=-1).count()

        return upvotes - downvotes


class PersonProposalTestcase(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        model = apps.get_model('votesystem', 'TopicProposal')
        enable_voting_on(model)
        cls.url = reverse('topic_proposal_list')

    def test_vote_is_blocked_when_month_has_proposed_meetup(self):
        topic_proposal = TopicProposalBuilder().build()
        proposed_meetup = ProposedMeetupBuilder().with_topic_proposal(topic_proposal).build()
        header = '<th>Vote</th>'
        link = f'<a href="{self.url}?vote_for={topic_proposal.pk}">vote</a>'
        response = self.client.get(self.url)

        self.assertNotContains(response, header, status_code=200, msg_prefix='', html=False)
        self.assertNotContains(response, link, status_code=200, msg_prefix='', html=False)

from django.apps import apps
from django.test import TestCase
from django.urls import reverse
from freezegun import freeze_time
from meetupselector.secretballot import enable_voting_on

from ..models import ProposedPonent, TopicProposal, TopicProposalLevel
from .builders import ProposedMeetupBuilder, TopicProposalBuilder


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
        cls.topic_proposal = TopicProposalBuilder().build()

    def test_vote_is_blocked_when_month_has_proposed_meetup(self):
        ProposedMeetupBuilder().with_topic_proposal(self.topic_proposal).build()
        header = '<th>Vote</th>'
        link = f'<a href="{self.url}?vote_for={self.topic_proposal.pk}">vote</a>'

        response = self.client.get(self.url)

        self.assertNotContains(response, header, status_code=200, html=False)
        self.assertNotContains(response, link, status_code=200, html=False)

    @freeze_time("2020-10-01 14:00:00")
    def test_vote_is_unblocked_when_proposed_meetup_is_the_month_before(self):
        ProposedMeetupBuilder().with_topic_proposal(self.topic_proposal).with_month(9).build()

        header = '<th>Vote</th>'
        link = f'<a href="{self.url}?vote_for={self.topic_proposal.pk}">vote</a>'
        response = self.client.get(self.url)

        self.assertContains(response, header, status_code=200, html=False)
        self.assertContains(response, link, status_code=200, html=False)

    def test_it_renders_proposed_ponent_form(self):
        ProposedMeetupBuilder().with_topic_proposal(self.topic_proposal).build()

        fragments = [
            '<label for="id_name">',
            '<label for="id_email">',
            '<label for="id_proposed_meetup">'
        ]

        response = self.client.get(self.url)
        for fragment in fragments:
            self.assertContains(response=response, text=fragment, status_code=200)

    def test_post_successful(self):
        proposed_meetup = ProposedMeetupBuilder().with_topic_proposal(self.topic_proposal).build()

        data = {
            "name": "Wozniack",
            "email": "Siliconvalley@gmail.com",
            "proposed_meetup": proposed_meetup.id
        }

        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)

    def test_post_successful_creates_object(self):
        proposed_meetup = ProposedMeetupBuilder().with_topic_proposal(self.topic_proposal).build()
        data = {
            "name": "Wozniack",
            "email": "Siliconvalley@gmail.com",
            "proposed_meetup": proposed_meetup.id
        }

        self.client.post(self.url, data)

        proposed = ProposedPonent.objects.first()
        self.assertIsNotNone(proposed)
        self.assertEquals(proposed.name, data["name"])
        self.assertEquals(proposed.email, data["email"])

    def test_post_invalid(self):
        ProposedMeetupBuilder().with_topic_proposal(self.topic_proposal).build()

        data = {
            "name": "",
            "email": "",
            "proposed_meetup": ""
        }

        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 400)

    def test_if_proposed_ponent_exists_not_render_form(self):
        proposed_meetup = ProposedMeetupBuilder().with_topic_proposal(self.topic_proposal).build()
        ProposedPonent.objects.create(name='Wozniack', email='Siliconvalley@gmail.com', proposed_meetup=proposed_meetup)

        response = self.client.get(self.url)

        self.assertNotContains(response, '<label for="id_proposed_meetup">', html=True)

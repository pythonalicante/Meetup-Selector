from django.utils import timezone

from ..models import (
    TopicProposal,
    TopicProposalLevel,
    ProposedMeetUp
)


class TopicProposalBuilder:

    def __init__(self):
        self.__topic = 'Any topic'
        self.__description = 'Any description'
        self.__level = TopicProposalLevel.BASIC
        self.__total_votes = 0

    def with_topic(self, topic):
        self.__topic = topic
        return self

    def with_description(self, description):
        self.__description = description
        return self

    def with_level(self, level):
        self.__level = level
        return self

    def with_total_votes(self, total_votes):
        self.__total_votes = total_votes
        return self

    def build(self):

        topic_proposal = TopicProposal.objects.create(
            topic=self.__topic,
            description=self.__description,
            level=self.__level
        )

        if self.__total_votes > 0:
            for i in range(self.__total_votes):
                token = f'anything{topic_proposal.id}{i}'
                topic_proposal.add_vote(token, 1)

        return topic_proposal


class ProposedMeetupBuilder:

    def __init__(self):
        self.__topic_proposal = None
        self.__year = timezone.now().year
        self.__month = timezone.now().month

    def with_topic_proposal(self, topic_proposal):
        self.__topic_proposal = topic_proposal
        return self

    def with_month(self, month):
        self.__month = month
        return self

    def with_year(self, year):
        self.__year = year
        return self

    def build(self):
        return ProposedMeetUp.objects.create(topic_proposal=self.__topic_proposal, year=self.__year, month=self.__month)

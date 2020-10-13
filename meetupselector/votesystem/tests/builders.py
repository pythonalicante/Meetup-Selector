from ..models import (
    TopicProposal,
    TopicProposalLevel
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

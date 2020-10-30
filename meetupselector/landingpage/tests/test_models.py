from django.test import TestCase

from ..models import Collaborator, SocialNetwork


class ModelsLandingPageTestcase(TestCase):
    def setUp(self):
        Collaborator.objects.create(
            first_name="John",
            last_name="Doe",
            email="prueba@prueba.com",
            nationality="test",
        )
        SocialNetwork.objects.create(
            collaborator=Collaborator.objects.get(id=1),
            network="Github",
            link="https://github.com/",
        )

    def test_return_full_name_collaborator(self):
        collaborator = Collaborator.objects.get(id=1)
        expected_object_full_name = "%s %s" % (
            collaborator.first_name,
            collaborator.last_name,
        )
        self.assertEquals(expected_object_full_name, str(collaborator))

    def test_return_network_name_socialnetwork(self):
        network = SocialNetwork.objects.get(id=1)
        expected_object_network_name = "%s" % (network.network)
        self.assertEquals(expected_object_network_name, str(network))

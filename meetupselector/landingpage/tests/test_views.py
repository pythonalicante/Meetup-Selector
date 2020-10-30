import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from ..models import Content

from ..models import Collaborator, SocialNetwork


class LandingPageTestcase(TestCase):

    url = reverse("home")

    def test_it_serves_home_view(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)

    def test_it_renders_landing_page(self):
        response = self.client.get(self.url)

        fragment = "You can change the content in the admin page"

        self.assertContains(response=response, text=fragment, status_code=200)
        
    def test_it_renders_landing_page_contents(self):
        Content.objects.create(
            title='Any title',
            content='Any content'
        )

        response = self.client.get(self.url)

        self.assertContains(response=response, text='Any title', status_code=200)
        self.assertContains(response=response, text='Any content', status_code=200)

    def test_it_renders_landing_page_contents_ordering_newest_first(self):
        old_content = Content.objects.create(
            content='Old content'
        )
        old_content.date_added = timezone.now() - datetime.timedelta(days=1)
        Content.objects.create(
            content='New content'
        )

        response = self.client.get(self.url)

        content = str(response.content)
        new_content_position = content.find('New content')
        old_content_position = content.find('Old content')

        self.assertTrue(new_content_position >= 0)
        self.assertTrue(old_content_position >= 0)
        self.assertTrue(new_content_position < old_content_position)     


class CollaboratorTestcase(TestCase):
    def setUp(self):
        self.url = reverse("collaborator_list")
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
        self.collaborator = Collaborator.objects.get(id=1)
        self.network = SocialNetwork.objects.filter(collaborator=self.collaborator)
        self.response = self.client.get(self.url)

    def test_it_serves_collaborator_list_view(self):
        self.assertEqual(self.response.status_code, 200)

    def test_collaborator_list_exists_in_the_template_collaborator_list(self):
        self.assertTrue("collaborators" in self.response.context)

    def test_collaborator_exists_in_the_collaborator_list(self):
        self.assertTrue(self.collaborator in self.response.context["collaborators"])

    def test_collaborator_exists_in_the_collaborator_detail(self):
        collaborator_detail_url = reverse("collaborator", args=[self.collaborator.pk])
        collaborator_data = self.client.get(collaborator_detail_url)
        self.assertEquals(self.collaborator, collaborator_data.context["collaborator"])


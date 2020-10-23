from django.test import TestCase
from django.urls import reverse


class LandingPageTestcase(TestCase):
    url = reverse('home')

    def test_it_serves_home_view(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
    
    def test_it_renders_landing_page(self):
        response = self.client.get(self.url)

        fragment = 'Python Alicante'

        self.assertContains(response=response, text=fragment, status_code=200)
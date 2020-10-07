from django.test import TestCase
from django.urls import reverse

from ..models import TopicProposalLevel


class TopicProposalTestcase(TestCase):
    url = reverse('topic_proposal')

    def test_it_serves_topic_proposal_view(self):
        response = self.client.get(reverse('topic_proposal'))

        self.assertEqual(response.status_code, 200)

    def test_it_renders_form(self):
        form_html = f"""
            <form action="{self.url}" method="post">
              <p>
                <label for="id_topic">Topic:</label>
                <input type="text" name="topic" maxlength="250" required id="id_topic" />
                <span class="helptext">Topic</span>
              </p>
              <p>
                <label for="id_description">Description:</label>
                <textarea
                  name="description"
                  cols="40"
                  rows="10"
                  maxlength="250"
                  required
                  id="id_description"
                >
                </textarea>
                <span class="helptext">Short description</span>
              </p>
              <p>
                <label for="id_level">Level:</label>
                <select name="level" id="id_level">
                  <option value="BASIC" selected>Basic</option>

                  <option value="INTERMEDIATE">Intermediate</option>

                  <option value="ADVANCED">Advanced</option>
                </select>
              </p>
              <input type="submit" value="Submit" />
            </form>
        """

        response = self.client.get(self.url)

        self.assertContains(response=response, text=form_html, status_code=200, html=True)

    def test_post_successful(self):
        data = {
            "topic": "Something interesting",
            "description": "This is a very interesting topic I think should be presented",
            "level": TopicProposalLevel.BASIC
        }

        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 200)

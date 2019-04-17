from django.test import TestCase


class HomePageTest(TestCase):

    def test_uses_home_templated(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
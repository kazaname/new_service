from django.test import TestCase
from django.core.urlresolvers import resolve
from .views import HomeView


class HomePageTest(TestCase):

    def test_root_url_resolve_to_home_view(self):
        response = self.client.get('/')
        found = resolve('/')

        self.assertEqual(response.status_code, 200)
        self.assertTrue(found.func, HomeView.as_view)
        self.assertTemplateUsed(response, 'base.html')

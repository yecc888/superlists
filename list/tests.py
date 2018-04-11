from django.test import TestCase
from django.core.urlresolvers import resolve
from list.views import home_page


# Create your tests here
class SmokeTest(TestCase):

    def test_root_rul(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

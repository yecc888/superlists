from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from list.views import home_page


# Create your tests here
class SmokeTest(TestCase):

    def test_root_rul(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_some(self):
        request = HttpRequest()
        respones = home_page(request)
        self.assertTrue(respones.content.startswith(b'<html>'))
        self.assertIn(b'<title>TO-DO list</title>', respones.content)
        self.assertTrue(respones.content.endswith(b'</html>'))

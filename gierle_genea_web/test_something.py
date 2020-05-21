from django.test import TestCase

from gierle_genea_web import urls


class SomeTestCase(TestCase):
    def test_something(self):
        self.assertEquals(len(urls.urlpatterns), 1)

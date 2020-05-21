from django.test import TestCase

from django.urls import resolve

from genea_viewer.models import Person
from genea_viewer.views import index


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve("/")
        self.assertEqual(found.func, index)


class PersonModelTestCase(TestCase):
    def setUp(self):
        Person.objects.create(name="Jacobus")

    def test_person_has_a_name(self):
        person = Person.objects.get(name="Jacobus")
        self.assertEquals(person.name, "Jacobus")
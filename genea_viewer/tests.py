from django.test import TestCase
from datetime import datetime, date, timezone
from django.urls import resolve

from genea_viewer.models import Person
from genea_viewer.views import index, add_person


class TestAllURLs(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve("/")
        self.assertEqual(found.func, index)

    def test_add_person_url_resolves_to_add_person_page_view(self):
        found = resolve("/add_person")
        self.assertEqual(found.func, add_person)


class PersonModelTestCase(TestCase):
    def setUp(self):
        Person.objects.create(name="Jacobus", date_of_birth=datetime(2020, 1, 1, 0, 0, tzinfo=timezone.utc))

    def test_person_has_a_name(self):
        person = Person.objects.get(name="Jacobus")
        self.assertEquals(person.name, "Jacobus")

    def test_person_has_birthdate(self):
        person = Person.objects.get(date_of_birth=datetime(2020, 1, 1, 0, 0, tzinfo=timezone.utc))
        self.assertEquals(person.date_of_birth, datetime(2020, 1, 1,tzinfo=timezone.utc))

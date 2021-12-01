from django.test import TestCase

from .models import Person


class DataTestCase(TestCase):
    def setUp(self):
        Person.objects.create(name="Stefan", surname="Roger", age=20, weight=64, height=174)
        Person.objects.create(name="Andrew", surname="Bernard", age=32, weight=55, height=164)

    def test_if_created(self):
        r = Person.objects.get(name="Stefan")
        self.assertEqual(r.name, "Stefan")
        self.assertEqual(r.weight, 64)
        self.assertEqual(r.surname, "Roger")
        self.assertNotEqual(r.age, 202)
        self.assertEqual(r.height, 174)
        self.assertEqual(Person.objects.all().count(), 2)

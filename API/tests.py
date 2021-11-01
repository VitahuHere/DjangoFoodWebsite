from django.test import TestCase, Client
from accounts.models import Person


class TestResponse(TestCase):
    def setUp(self):
        Person.objects.create(name="Stefan", surname="Curry", age=25, weight=64, height=174)

    def test_person_creation(self):
        self.assertEqual(Person.objects.all().count(), 1)

    def test_api_get(self):
        c = Client()
        pk = int(input())
        r = c.get(f'http://localhost:8000/API/get/account/data/{pk}')
        print(r)
from django.test import TestCase, Client

from accounts.models import Person


class TestResponse(TestCase):
    def setUp(self):
        Person.objects.create(name="Stefan", surname="Curry", birthday='2002-11-12', weight=64, height=174)

    def test_person_creation(self):
        self.assertEqual(Person.objects.all().count(), 1)

    def test_creating_person(self):
        c = Client()
        r = c.post('http://localhost:8000/api/post/account',
                   {'name': 'Stefan',
                    'surname': 'Curry',
                    'birthday': '2002-11-12',
                    'weight': 64,
                    'height': 174
                    }
                   )
        print(r.POST)


"""
{'name': 'Stefan', 'surname': 'Curry', 'birthday': '2002-11-12', 'weight': 64, 'height': 174}
"""

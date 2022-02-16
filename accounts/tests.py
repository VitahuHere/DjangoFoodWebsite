from django.test import TestCase
import datetime

from .models import Person
from packages.models import Package


class AccountTestCase(TestCase):
    def setUp(self):
        Person.objects.create(
            login="login",
            password="password",
            name="Andrew",
            surname="Stewart",
            birthday=datetime.date(year=2000, month=10, day=23),
            address="London street 123"
        )

    def test_person_creation(self):
        andrew = Person.objects.get(name="Andrew")
        self.assertEqual(andrew.surname, "Stewart")
        self.assertEqual(andrew.login, "428821350e9691491f616b754cd8315fb86d797ab35d843479e732ef90665324")
        self.assertEqual(andrew.password, "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8")
        self.assertEqual(andrew.birthday, datetime.date(year=2000, month=10, day=23))



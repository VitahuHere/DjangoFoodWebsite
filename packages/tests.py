import datetime

from django.test import TestCase
from .models import Package
from accounts.models import Person


class TestPackages(TestCase):
    def setUp(self):
        Person.objects.create(
            login="login",
            password="password",
            name="Andrew",
            surname="Stewart",
            birthday=datetime.date(year=2000, month=10, day=23),
            address="London street 123"
        )

    def test_package_creation(self):
        p = Person.objects.get(name="Andrew")
        Package.objects.create(
            client=p,
            address="Jerusalem 123",
            title="Schab",
            contents=[
                "600g boneless porkchop",
                "flour",
                "2 eggs",
                "bread crumbs",
                "oil",
                "milk",
            ]
        )
        self.assertEqual(Package.objects.count(), 1)
        self.assertEqual(len(Package.objects.get(client=p).contents), 6)

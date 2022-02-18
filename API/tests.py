import datetime
from hashlib import sha256
from django.test import TestCase, Client

from accounts.models import Account
from packages.models import Package, Product
from rest_framework.authtoken.models import Token


class TestAccount(TestCase):
    def setUp(self):
        self.c = Client()
        a = Account.objects.create(
            login="login",
            password="password",
            name="Andrew",
            surname="Stewart",
            birthday=datetime.date(year=2000, month=10, day=23),
            address="London street 123",
        )
        Token.objects.create(user=a).save()
        self.tk = Token.objects.get(user=a)

    def test_obtaining_token(self):
        payload = {
            "login": str(sha256("login".encode()).hexdigest()),
            "password": str(sha256("password".encode()).hexdigest())
        }
        r = self.c.post('/api/post/auth-token/',
                        data=payload)
        self.assertEqual(r.status_code, 401)

        payload["token"] = self.tk.key
        r = self.c.post('api/post/auth-token',
                        data=payload)
        self.assertEqual(r.status_code, 200)
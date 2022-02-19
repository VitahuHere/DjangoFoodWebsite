import datetime

from rest_framework.test import APITestCase

from accounts.models import Account
from packages.models import Package, Product
from .models import AccountToken

from rest_framework.test import APIClient


class TestToken(APITestCase):
    def setUp(self):
        self.user = Account.objects.create(
            login="login",
            password="password",
            name="Andrew",
            surname="Stewart",
            birthday=datetime.date(year=2000, month=10, day=23),
            address="London street 123",
        )

    def test_obtaining_token(self):
        client = APIClient()
        payload = {
            'login': '428821350e9691491f616b754cd8315fb86d797ab35d843479e732ef90665324',
            'password': '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8',
        }
        # valid credentials
        response = client.post('/api/post/obtain-auth-token/', data=payload)
        assert 'Token' in response.data['token']
        # invalid credentials
        payload['login'] = 'invalid'
        response = client.post('/api/post/obtain-auth-token/', data=payload)
        self.assertEqual(response.status_code, 400)
        client.logout()

    def test_receiving_token(self):
        client = APIClient()
        AccountToken.objects.create(user=self.user).save()
        tk = AccountToken.objects.get(user=self.user).key
        payload = {
            'login': '428821350e9691491f616b754cd8315fb86d797ab35d843479e732ef90665324',
            'password': '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8',
        }
        r = client.post('/api/post/obtain-auth-token/', data=payload)
        self.assertEqual(r.status_code, 200)
        parse = r.data['token'].split()[1]
        self.assertEqual(parse, tk)
        client.logout()


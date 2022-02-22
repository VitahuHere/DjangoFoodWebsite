import datetime

from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from packages.models import Package, Product
from accounts.models import Account
from .models import AccountToken


class TestToken(APITestCase):
    def setUp(self) -> None:
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
        endpoint = '/api/obtain-auth-token/'
        payload = {
            'login': '428821350e9691491f616b754cd8315fb86d797ab35d843479e732ef90665324',
            'password': '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8',
        }
        # valid credentials
        response = client.post(endpoint, data=payload)
        assert response.data['token']
        # invalid credentials
        payload['login'] = 'invalid'
        response = client.post(endpoint, data=payload)
        self.assertEqual(response.status_code, 403)
        client.logout()

    def test_receiving_token(self):
        client = APIClient()
        AccountToken.objects.create(user=self.user).save()
        tk = AccountToken.objects.get(user=self.user).key
        payload = {
            'login': '428821350e9691491f616b754cd8315fb86d797ab35d843479e732ef90665324',
            'password': '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8',
        }
        r = client.post('/api/obtain-auth-token/', data=payload)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data['token'], tk)
        client.logout()


class TestAccountInformation(APITestCase):
    def setUp(self) -> None:
        self.user = Account.objects.create(
            login="login",
            password="password",
            name="Andrew",
            surname="Stewart",
            birthday=datetime.date(year=2000, month=10, day=23),
            address="London street 123",
        )

    def test_accessing_data(self):
        token = AccountToken.objects.create(user=self.user)
        client = APIClient()
        endpoint = '/api/get-account-data/'
        payload = {
            'login': '428821350e9691491f616b754cd8315fb86d797ab35d843479e732ef90665324',
            'password': '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8',
        }
        # request without token
        r = client.get(endpoint, data=payload)
        self.assertEqual(r.status_code, 403)
        # request with token
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        r = client.get(endpoint, data=payload)
        self.assertEqual(r.status_code, 200)
        client.logout()


class TestPackages(APITestCase):
    def setUp(self):
        self.user = Account.objects.create(
            login="login",
            password="password",
            name="Andrew",
            surname="Stewart",
            birthday=datetime.date(year=2000, month=10, day=23),
            address="London street 123",
        )

    def test_creating_package(self):
        token = AccountToken.objects.create(user=self.user)
        c = APIClient()
        endpoint = '/api/create-package/'
        payload = {
            'login': 'invalid',
            'password': '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8',
        }

        # posting without token, invalid package details and invalid credentials
        response = c.post(endpoint, data=payload)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.data['detail'], 'Authentication credentials were not provided.')

        # posting with valid credentials, invalid package details but without token
        payload['login'] = '428821350e9691491f616b754cd8315fb86d797ab35d843479e732ef90665324'
        response = c.post(endpoint, data=payload)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.data['detail'], 'Authentication credentials were not provided.')

        # posting with correct package details and valid credentials but without token
        payload['address'] = 'Jerozolimskie 123 Warsaw'
        payload['title'] = ''
        payload['contents'] = [
            {'spaghetti: 500'},
            {'canned tomatoes: 400'},
            {'garlic: 5'}
        ]
        response = c.post(endpoint, data=payload)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.data['detail'], 'Authentication credentials were not provided.')

        # posting with token, valid package details but invalid credentials
        c.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        payload['login'] = 'invalid'
        response = c.post(endpoint, data=payload)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.data['detail'], 'Invalid credentials')

        # posting with valid credentials, valid package details and token
        payload['login'] = '428821350e9691491f616b754cd8315fb86d797ab35d843479e732ef90665324'
        response = c.post(endpoint, data=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['detail'], 'Successfully created package')

        c.logout()

        def test_package_status():
            ...
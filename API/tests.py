import datetime

from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from packages.models import Package, Product, Status
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

    def test_package_status(self):
        token = AccountToken.objects.create(user=self.user)
        state = Status.objects.create(pk="Package ready, waiting for delivery")
        Package.objects.create(
            client=self.user,
            address="Jerozolimskie 123 Warsaw",
            title="nothing",
            contents=[
                {'spaghetti: 500'},
                {'canned tomatoes: 400'},
                {'garlic: 5'},
            ],
            status=state,
        )
        c = APIClient()
        endpoint = '/api/check-package-status/'

        # getting package status with invalid credentials, without package id and without token
        payload = {
            'login': 'invalid',
            'password': '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8',
        }
        response = c.get(endpoint, data=payload)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.data['detail'], 'Authentication credentials were not provided.')

        # getting package status with valid credentials but without package id and without token
        payload = {
            'login': '428821350e9691491f616b754cd8315fb86d797ab35d843479e732ef90665324',
            'password': '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8',
        }
        response = c.get(endpoint, data=payload)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.data['detail'], 'Authentication credentials were not provided.')

        # getting package status with token but invalid credentials and without package id
        payload = {
            'login': 'invalid',
            'password': '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8',
        }
        c.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = c.get(endpoint, data=payload)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.data['detail'], 'Invalid credentials')

        # getting package status with token and valid credentials but without package id
        payload = {
            'login': '428821350e9691491f616b754cd8315fb86d797ab35d843479e732ef90665324',
            'password': '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8',
        }
        response = c.get(endpoint, data=payload)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.data['detail'], 'Missing package id')

        # getting package status with token and valid credentials but invalid package id
        payload = {
            'login': '428821350e9691491f616b754cd8315fb86d797ab35d843479e732ef90665324',
            'password': '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8',
            'id': 404,
        }
        response = c.get(endpoint, data=payload)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['detail'], 'Package does not exist')

        # getting package status with token and valid credentials
        payload = {
            'login': '428821350e9691491f616b754cd8315fb86d797ab35d843479e732ef90665324',
            'password': '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8',
            'id': 2,
        }
        response = c.get(endpoint, data=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['detail'], 'Package ready, waiting for delivery')


class TestProducts(APITestCase):
    def setUp(self) -> None:
        self.user = Account.objects.create(
            login="login",
            password="password",
            name="Andrew",
            surname="Stewart",
            birthday=datetime.date(year=2000, month=10, day=23),
            address="London street 123",
        )

    def test_product_creation(self):
        c = APIClient()
        token = AccountToken.objects.create(user=self.user)
        endpoint = '/api/create-product/'

        # posting with missing product data, no credentials and without token
        payload = {
            'name': 'Carrot',
            'net_weight': 60,
            'is_liquid': False,
        }
        response = c.post(endpoint, data=payload)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.data['detail'], 'Authentication credentials were not provided.')

        # posting with missing product data, correct credentials, but without token
        payload = {
            'login': '428821350e9691491f616b754cd8315fb86d797ab35d843479e732ef90665324',
            'password': '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8',
            'amount': 500,
            'net_weight': 60,
            'allergens': [{}]
        }
        response = c.post(endpoint, data=payload)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.data['detail'], 'Authentication credentials were not provided.')

        # posting with correct data, correct credentials, but without token
        payload = {
            'login': '428821350e9691491f616b754cd8315fb86d797ab35d843479e732ef90665324',
            'password': '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8',
            'name': 'Carrot',
            'amount': 500,
            'net_weight': 60,
            'is_liquid': False,
            'allergens': [{}]
        }
        response = c.post(endpoint, data=payload)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.data['detail'], 'Authentication credentials were not provided.')

        # posting with incorrect data, without credentials, but with token
        c.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        payload = {
            'amount': 500,
            'is_liquid': False,
            'allergens': [{}]
        }
        response = c.post(endpoint, data=payload)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.data['detail'], 'Invalid credentials')

        # posting with correct data, token but without credentials
        payload = {
            'name': 'Carrot',
            'amount': 500,
            'net_weight': 60,
            'is_liquid': False,
            'allergens': [{}]
        }
        response = c.post(endpoint, data=payload)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.data['detail'], 'Invalid credentials')

        # posting with correct data, valid credentials and token
        payload = {
            'login': '428821350e9691491f616b754cd8315fb86d797ab35d843479e732ef90665324',
            'password': '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8',
            'name': 'Carrot',
            'amount': 500,
            'net_weight': 60,
            'is_liquid': False,
            'allergens': [{}]
        }
        response = c.post(endpoint, data=payload)
        print(response.data['detail'])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['detail'], 'Product added successfully')

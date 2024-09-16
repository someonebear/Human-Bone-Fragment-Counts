from django.test import TestCase, Client
import json
from django.core.management import call_command
# Create your tests here.


# class SignupTestCase(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.client.post(
#             "/auth/users/", {"username": "testuser", "password": "unCOMMON1234", "re_password": "unCOMMON1234"},)

#     def test_create_user(self):
#         response = self.client.post(
#             "/auth/users/", {"username": "testuser1", "password": "unCOMMON1234", "re_password": "unCOMMON1234"},)
#         self.assertEqual(response.status_code, 201)

#     def test_login(self):
#         response = self.client.post(
#             "/auth/token/login", {"username": "testuser", "password": "unCOMMON1234"},)
#         self.assertEqual(response.status_code, 200)


class EntryTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.post(
            "/auth/users/", {"username": "testuser", "password": "unCOMMON1234", "re_password": "unCOMMON1234"},)
        call_command('loaddata', 'elements')
        call_command('loaddata', 'landmarks')
        call_command('loaddata', 'sites')
        call_command('loaddata', 'spits')

    def test_create_entryGroup_entry(self):
        response = self.client.post(
            "/auth/token/login/", {"username": "testuser", "password": "unCOMMON1234"},)
        token = response.data["auth_token"]
        entryGroup = {
            "acc_num": 1,
            "sex": "Female",
            "age": "Infant",
            "entry_type": "Individual",
            "site": 1,
            "spit": 1
        }
        response = self.client.post(
            "/entry-groups/", json.dumps(entryGroup), headers={"Authorization": f"Token {token}"}, content_type="application/json")
        self.assertEqual(response.status_code, 201)
        entry = {
            "acc_num": 1,
            "bone": 1,
            "side": "Left",
            "size": "2-5cm",
            "generic": True,
            "complete": 2,
            "landmarks": [4]
        }
        response = self.client.post(
            "/entries/", json.dumps(entry), headers={"Authorization": f"Token {token}"}, content_type="application/json")
        self.assertEqual(response.status_code, 201)

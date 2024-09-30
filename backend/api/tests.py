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
    fixtures = ['elements', 'landmarks', 'sites', 'spits']

    def setUp(self):
        self.client = Client()
        self.client.post(
            "/auth/users/", {"username": "testuser", "password": "unCOMMON1234", "re_password": "unCOMMON1234"},)

    def test_create_entryMeta(self):
        response = self.client.post(
            "/auth/token/login/", {"username": "testuser", "password": "unCOMMON1234"},)
        token = response.data["auth_token"]
        entryMeta = {
            "sex": "Female",
            "age": "Infant",
            "site": 1,
            "spit": 1
        }
        response = self.client.post(
            "/entry-meta/", json.dumps(entryMeta), headers={"Authorization": f"Token {token}"}, content_type="application/json")
        self.assertEqual(response.status_code, 201)
        entry = {
            "meta": response.data["pk"],
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

    def test_create_body_part(self):
        response = self.client.post(
            "/auth/token/login/", {"username": "testuser", "password": "unCOMMON1234"},)
        token = response.data["auth_token"]
        entryMeta = {
            "sex": "Female",
            "age": "Infant",
            "site": 1,
            "spit": 1
        }
        response = self.client.post(
            "/entry-meta/", json.dumps(entryMeta), headers={"Authorization": f"Token {token}"}, content_type="application/json")
        self.assertEqual(response.status_code, 201)
        meta_pk = response.data["pk"]

        body_part = {
            "bp_code": "BP1",
            "meta": meta_pk,
        }
        response = self.client.post(
            "/body-parts/", json.dumps(body_part), headers={"Authorization": f"Token {token}"}, content_type="application/json")
        self.assertEqual(response.status_code, 201)

        entry = {
            "meta": meta_pk,
            "body_part": "BP1",
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

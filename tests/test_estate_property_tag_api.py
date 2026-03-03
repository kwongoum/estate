import json
from odoo.tests import tagged
import requests
from odoo.tests import HttpCase
import random


@tagged("estate")
class TestEstatePropertyTagAPI(HttpCase):
    def setUp(self):
        super(TestEstatePropertyTagAPI, self).setUp()
        self.base_url = "http://localhost:8069"
        self.auth_token = "7328b3f1-6765-4515-85e6-80d4ff7de947"
        self.session_id = self.authenticate()

    def authenticate(self):
        url = f"{self.base_url}/web/session/authenticate"
        headers = {"Content-Type": "application/json"}
        data = {
            "jsonrpc": "2.0",
            "method": "call",
            "id": 1,
            "params": {
                "db": "learn-odoo-17",
                "login": "admin",
                "password": "admin",
            },
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))

    #  return response

    # ============

    def test_get_tags(self):
        url = f"{self.base_url}/estate-property-tags"
        headers = {
            "Authorization": self.auth_token,
            "Cookie": f"session_id={self.session_id}",
        }
        response = requests.get(url, headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_get_tag_by_id(self):
        tag_id = 2
        url = f"{self.base_url}/estate-property-tag/{tag_id}"
        headers = {
            "Authorization": self.auth_token,
            "Cookie": f"session_id={self.session_id}",
        }

        response = requests.get(url, headers=headers)
        self.assertEqual(response.status_code, 200)

        expected_response = {"id": 2, "name": "Green", "color": 2}
        self.assertEqual(response.json(), expected_response)

        # create ======

    def test_create_tag(self):
        url = f"{self.base_url}/estate-property-tag"
        headers = {
            "Authorization": self.auth_token,
            "Cookie": f"session_id={self.session_id}",
        }
        random_number = random.random()
        data = {"name": f"named{random_number}", "color": 99}

        response = requests.post(url, headers=headers, data=json.dumps(data))
        self.assertEqual(response.status_code, 200)

        # update

    def test_update_tag(self):
        updated_id = 1
        url = f"{self.base_url}/estate-property-tag/{updated_id}"
        headers = {
            "Authorization": self.auth_token,
            "Cookie": f"session_id={self.session_id}",
        }
        data = {"name": "nameUPDT", "color": 11}
        response = requests.put(url, headers=headers, data=json.dumps(data))
        self.assertEqual(response.status_code, 200)
        expected_response = {"id": updated_id, "name": "nameUPDT", "color": 11}
        self.assertEqual(response.json(), expected_response)

        # delete

    def test_delete_tag(self):
        delete_id = 68
        url = f"{self.base_url}/estate-property-tag/{delete_id}"
        headers = {
            "Authorization": self.auth_token,
            "Cookie": f"session_id={self.session_id}",
        }
        response = requests.delete(url, headers=headers)
        self.assertEqual(response.status_code, 200)

        expected_response = {
            "id": delete_id,
            "message": f"Tag with id n° {delete_id} has been deleted.",
        }
        self.assertEqual(response.json(), expected_response)

        # unauthorized request ====

    def test_unauthorized_request(self):
        url = f"{self.base_url}/estate-property-tags"
        response = requests.get(url)
        self.assertEqual(response.status_code, 401)
        self.assertIn("Un-authorized", response.text)

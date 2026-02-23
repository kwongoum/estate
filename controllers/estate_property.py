import json
import requests
from odoo import http


class EstateProperty(http.Controller):

    @http.route("/welcome", auth="public", methods=["GET", "POST"])
    def healthcheck(self, **kw):
        return "IT Works: message for anyone: public, user"

    @http.route("/profil", auth="user")
    def xyz(self, **kw):
        return " It's authenticated: message for authenticated user"

    @http.route("/api/users", auth="user", type="json", methods=["GET"])
    def get_users(self, **kwargs):
        users = requests.env["res.users"].search([])
        result = []
        for user in users:
            result.append({"id": user.id, "name": user.name, "email": user.login})
        return result

    @http.route("/entries", auth="public")
    def entries(self, **kw):
        response = requests.get(
            "https://collectionapi.metmuseum.org/public/collection/v1/objects/100"
        )
        return json.dumps(response.json())

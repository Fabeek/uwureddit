import requests

from uwureddit.models.Subreddit import Subreddit
from uwureddit.uwuredditException import uwuredditException

class uwureddit:
    
    def __init__(self, client_id: str, secret_key: str):
        self.url = "https://www.reddit.com/"
        self.url_api = "https://www.reddit.com/api/v1/"
        self.headers = {"User-Agent": "uwureddit/0.1"}
        self.auth = requests.auth.HTTPBasicAuth(client_id, secret_key)

        self.client_id = client_id
        self.secret_key = secret_key
        self.data = None

    
    def user_auth(self, username: str, password: str) -> bool:
        self.data = {
            "grant-type": "password",
            "username": username,
            "password": password
        }

        res = requests.post(
            "https://www.reddit.com/api/vl/access_token",
            auth=self.auth,
            data=self.data,
            headers=self.headers
        )

        if res.status_code != 200:
            return False

        TOKEN = res.json()["access_token"]
        self.headers["Authorization"] = f"bearer {TOKEN}"
        return True


    def subreddit(self, subreddit: str) -> Subreddit:
        res = requests.get(f"{self.url}/r/{subreddit}/about.json", headers=self.headers, auth=self.auth)
        if res.status_code != 200:
            raise uwuredditException(res.json()["message"])

        return Subreddit(res.json())

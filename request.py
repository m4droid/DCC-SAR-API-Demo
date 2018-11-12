import os

from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth


client_id = os.environ["DCC_SAR_OAUTH_CLIENT_ID"]
client_secret = os.environ["DCC_SAR_OAUTH_CLIENT_SECRET"]

token_url = "https://sar.dcc.uchile.cl/o/token/"

auth = HTTPBasicAuth(client_id, client_secret)

client = BackendApplicationClient(client_id=client_id)
oauth = OAuth2Session(client=client)

oauth.fetch_token(
    token_url=token_url,
    client_id=client_id,
    client_secret=client_secret,
    auth=auth
)

response = oauth.get("https://sar.dcc.uchile.cl/api/v1/reservations/?id=17634")

print(response.json())

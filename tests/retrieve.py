from __future__ import print_function

import os

from apiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools
import json

from rest_api.settings import BASE_DIR
from google_auth_oauthlib.flow import InstalledAppFlow


def retrieve_response(form_id):

    SCOPES = "https://www.googleapis.com/auth/forms.responses.readonly"
    DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

    print(str(BASE_DIR) + "/tests/token.json")
    store = file.Storage(str(BASE_DIR) + "/tests/token.json")
    creds = None
    if not creds or creds.invalid:
        secret = json.loads(os.environ["OAUTH_SECRET"])
        # flow = client.flow_from_clientsecrets(str(BASE_DIR) + "/tests/client_secrets.json", SCOPES)
        flow = InstalledAppFlow.from_client_config(secret, SCOPES)
        print("check4")
        creds = tools.run_flow(flow, store)
        print("check5")
    service = discovery.build('forms', 'v1', http=creds.authorize(
        Http()), discoveryServiceUrl=DISCOVERY_DOC, static_discovery=False)
    print("check6")

    # Prints the responses of your specified form:
    result = service.forms().responses().list(formId=form_id).execute()
    print("check7")
    return result

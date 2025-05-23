import requests
from requests.auth import HTTPBasicAuth
import os
from datetime import datetime


CONFLUENCE_DOMAIN = os.environ["CONFLUENCE_DOMAIN"]  # e.g. yourteam.atlassian.net
CONFLUENCE_EMAIL = os.environ["CONFLUENCE_EMAIL"]
CONFLUENCE_API_TOKEN = os.environ["CONFLUENCE_API_TOKEN"]
CONFLUENCE_SPACE = os.environ["CONFLUENCE_SPACE"]  # e.g. "DEV"
DATE_TIME = datetime.now()


def push_to_confluence_page(html_content, parent_id=None):

    url = f"https://{CONFLUENCE_DOMAIN}/wiki/rest/api/content/"

    headers = {
        "Content-Type": "application/json"
    }

    auth = HTTPBasicAuth(CONFLUENCE_EMAIL, CONFLUENCE_API_TOKEN)

    payload = {
        "type": "page",
        "title": f"Test Cases Summary: {DATE_TIME.strftime('%m-%d @ %H:%M')}",
        "space": {"key": CONFLUENCE_SPACE},
        "body": {
            "storage": {
                "value": html_content,
                "representation": "storage"
            }
        }
    }

    if parent_id:
        payload["ancestors"] = [{"id": parent_id}]

    response = requests.post(url, headers=headers, json=payload, auth=auth)

    if response.status_code == 200 or response.status_code == 201:
        print(f"✅ Page created successfully.")
    else:
        print(f"❌ Failed to create page: {response.status_code}")
        print(response.json())
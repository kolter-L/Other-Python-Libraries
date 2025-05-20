import requests
from Models.TestCase import TestCase
import os

TESTRAIL_DOMAIN = os.environ["TESTRAIL_DOMAIN"]
TESTRAIL_EMAIL = os.environ["TESTRAIL_EMAIL"]
TESTRAIL_API_KEY = os.environ["TESTRAIL_API_KEY"]

BASE_URL = f"https://{TESTRAIL_DOMAIN}/index.php?/api/v2"
AUTH = (TESTRAIL_EMAIL, TESTRAIL_API_KEY)
HEADERS = {"Content-Type": "application/json"}

# Get projects
def get_projects():
    response = requests.get(f"{BASE_URL}/get_projects", auth=AUTH)
    response.raise_for_status()
    projects = response.json()["projects"]
    return projects

# get test cases for each project
def get_all_test_cases():
    all_cases = []
    projects = get_projects()
    for project in projects:
        project_id = project["id"]
        project_name = project["name"]
        print(f"📁 Fetching test cases from project: {project_name} (ID {project_id})")

        # You can optionally filter by suite_id here if needed
        response = requests.get(f"{BASE_URL}/get_cases/{project_id}", auth=AUTH)
        if response.status_code != 200:
            print(f"❌ Failed to get cases for project {project_name}")
            continue

        cases = response.json()["cases"]
        print(f"   ➕ Retrieved {len(cases)} cases")
        for case in cases:
            test_case_object = TestCase(project_name, case["id"], case["title"], case.get("refs"))
            all_cases.append(test_case_object)

    return all_cases
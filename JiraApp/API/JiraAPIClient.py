import requests
from requests.auth import HTTPBasicAuth
from Models.JiraIssue import JiraIssue
from Models.JiraProject import JiraProject
import os

# Read about the JIRA API that is used here:
# https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/#about

# --- Replace these with your values ---
JIRA_EMAIL = os.environ["JIRA_EMAIL"]
JIRA_API_TOKEN = os.environ["JIRA_API_TOKEN"]
JIRA_DOMAIN = os.environ["JIRA_DOMAIN"]

def get_jira_projects():
    # Projects to be returned
    all_jira_projects = []

    # CREATE BASIC AUTH OBJECT USING HTTPBASICAUTH MEHTOD THAT IS BUILT INTO THE REQUESTS LIBRARY
    auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN)

# DEFINE CUSTOM HEADERS, WE TELL JIRA TO SEND THE DATA BACK TO US IN THE JSON FORMAT
    headers = {
        "Accept": "application/json"
    }

    # CREATE OUR URL AND MAKE A GET REQUEST FOR ALL PROJECTS
    projects_url = f"https://{JIRA_DOMAIN}/rest/api/3/project/search"
    projects_response = requests.get(projects_url, headers=headers, auth=auth)

    if projects_response.status_code != 200:
        print("Failed to fetch projects:", projects_response.status_code, projects_response.text)
        exit()

    projects = projects_response.json().get("values", [])
    print(f"Found {len(projects)} project(s).")

    # GET THE ISSUES FOR EACH PROJECT AND ADD THEM TO THE ISSUE OBJECT LIST
    for project in projects:
        project_object = JiraProject(project["name"], project["key"])

        # Fetch issues in this project
        issues_url = f"https://{JIRA_DOMAIN}/rest/api/3/search"
        params = {
        "jql": f'project = {project_object.project_key} AND status IN ("To Do", "In Progress")',
            "maxResults": 50
        }

        issues_response = requests.get(issues_url, headers=headers, params=params, auth=auth)
        if issues_response.status_code != 200:
            print(f"❌ Failed to get issues for {project_key}: {issues_response.status_code}")
            continue

        issues_json = issues_response.json().get("issues", [])
        for issue in issues_json:
            key = issue["key"]
            summary = issue["fields"]["summary"]
            issue_object = JiraIssue(key, summary)
            project_object.add_issue(issue_object)

        all_jira_projects.append(project_object)

    return all_jira_projects



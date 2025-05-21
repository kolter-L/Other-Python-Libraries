from dotenv import load_dotenv
load_dotenv()

from API.ConfluenceAPIClient import push_to_confluence_page
from API.JiraAPIClient import get_jira_projects
from API.TestRailAPIClient import get_all_test_cases
from Services.JiraProjectService import JiraProjectService
from Services.RenderingService import render_confluence_report

_project_service = JiraProjectService()

jira_projects = get_jira_projects()

test_cases = get_all_test_cases()

_project_service.map_test_cases_to_issues(jira_projects, test_cases)

rendered_doc = render_confluence_report(jira_projects)

# Push to Confluence
push_to_confluence_page(html_content=rendered_doc, parent_id=524290)  # or a real page ID if you want it nested



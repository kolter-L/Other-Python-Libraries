
class JiraProjectService:

    def __init__(self):
        pass

    def map_test_cases_to_issues(self, jira_projects, test_cases):
        """
        Matches test cases to Jira issues across all Jira projects.
        Updates each JiraIssue's test_cases list if its key is referenced in a test case.
        """
        # Flatten all Jira issues from all projects
        issue_lookup = {}
        for project in jira_projects:
            for issue in project.issues:
                issue_lookup[issue.key] = issue

        # Associate test cases with issues using refs
        for test_case in test_cases:
            if not test_case.refs:
                continue
            for ref in test_case.refs.split(","):
                ref = ref.strip()
                if ref in issue_lookup:
                    issue_lookup[ref].add_test_case(test_case)

from Models.JiraIssue import JiraIssue

class JiraProject:

    def __init__(self, name, key):
        self.project_name = name
        self.project_key = key
        self._jira_issues = []

    def add_issue(self, issue):
        if not isinstance(issue, JiraIssue):
            raise TypeError(f"Expected JiraIssue, got {type(issue).__name__}")
        self._jira_issues.append(issue)

    @property
    def issues(self):
        return self._jira_issues

    def __str__(self):
        issues_str = "\n".join(f"{str(issue)}" for issue in self._jira_issues) if self._jira_issues else "(no issues)"
        return f"Name: {self.project_name}\nKey: {self.project_key}\nIssues:\n{issues_str}"

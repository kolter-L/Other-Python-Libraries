

class JiraIssue:

    def __init__(self, key, summary):
        self.key = key
        self.summary= summary
        self.test_cases = []

    def add_test_case(self, test_case):
        self.test_cases.append(test_case)

    def __str__(self):
        test_case_lines = "\n".join(f"  - {tc}" for tc in self.test_cases)
        return f"Key: {self.key}\nSummary: {self.summary}\nTest Cases:\n{test_case_lines if self.test_cases else '  (none)'}"

        
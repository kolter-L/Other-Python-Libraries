
class TestCase:

    def __init__(self, project, id, title, refs):
        self.project = project
        self.id = id
        self.title = title
        self.refs = refs

    def __str__(self):
        return f"Title: {self.title}, Refs: {self.refs}"
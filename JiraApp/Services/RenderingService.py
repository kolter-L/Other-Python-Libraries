from jinja2 import Environment, FileSystemLoader
from Models.JiraProject import JiraProject
from Models.JiraIssue import JiraIssue
from Models.TestCase import TestCase  # your domain classes

def render_confluence_report(projects, output_path="test_report.html"):
    # Set up Jinja environment
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("confluence_template.xml")

    # Render the template with your data
    html_output = template.render(projects=projects)

    # Write to file
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_output)

    print(f"✅ Report written to: {output_path}")

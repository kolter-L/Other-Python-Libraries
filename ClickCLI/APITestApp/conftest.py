import pytest

# ADDS THE FLAG TO PYTEST 
# WE CAN NOW DO THIS AND FEED IN BASE URL:
# pytest --base-url http://yourapi.com

def pytest_addoption(parser):
    parser.addoption("--base-url", action="store", default="http://localhost:3000")


# THIS FIXTURE ALLOWS US TO FIND AND ACCESS THE OPTION ELSEWHERE
# THE NAME OF THE FUNCTION DEFINES THE NAME OF THE VARIABLE (BASE URL IN THIS CASE)
# REQUEST IS A SPECIAL KEYWORD THAT LETS US ACCESS THE CONFIG AND OPTIONS

@pytest.fixture
def base_url(request):
    return request.config.getoption("--base-url")

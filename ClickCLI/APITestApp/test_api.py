import os
import requests

'''
We are using the requests library; response objects are going to be returned
Here are some common attributes of the response object:

| Property / Method | What it does                                                  |
| ----------------- | ------------------------------------------------------------- |
| `r.status_code`   | HTTP status code (e.g. 200, 404)                              |
| `r.headers`       | Dictionary of response headers                                |
| `r.text`          | Response body as a string (raw text)                          |
| `r.content`       | Response body as bytes                                        |
| `r.json()`        | Parses response body as JSON (raises error if not valid JSON) |
| `r.url`           | Final URL after any redirects                                 |
| `r.reason`        | Status reason phrase (e.g. "OK")                              |
| `r.ok`            | `True` if status\\_code is < 400                               |
| `r.elapsed`       | Time taken for the request                                    |
| `r.cookies`       | Response cookies                                              |

'''

def test_get_orders(base_url):
    #base_url = os.getenv('PYTEST_BASE_URL', 'http://localhost:3000')
    r = requests.get(f"{base_url}/orders")
    assert r.status_code == 200

def test_get_tacos(base_url):
    r = requests.get(f"{base_url}/orders")
    print("This is the result of TACOS: ")
    tacos = []
    try:
        tacos = r.json()
    except ValueError:
        tacos = r.text

    assert isinstance(tacos, list)

    assert r.status_code == 200
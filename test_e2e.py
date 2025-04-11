import pytest
import requests
import open_api_parser as parser

host, api_tests = parser.parse_openapi_spec('openapi.json')
test_ids = [f"{ep['method']} {ep['path']}" for ep in api_tests]

def send_request(method, url):
    method = method.upper()
    if method == "GET":
        return requests.get(url)
    elif method == "POST":
        return requests.post(url)
    elif method == "PUT":
        return requests.put(url)
    elif method == "PATCH":
        return requests.patch(url)
    elif method == "DELETE":
        return requests.delete(url)
    else:
        raise ValueError(f"Unsupported HTTP method: {method}")

@pytest.mark.parametrize("test_case", api_tests, ids=test_ids)
def test_api_response_200(test_case):
    method = test_case["method"]
    endpoint = host+test_case["path"]

    response = send_request(method, endpoint)

    assert response.status_code == 200, f"{method} {endpoint} failed: {response.status_code}"

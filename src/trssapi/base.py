import requests

DEFAULT_URL = "https://iamtagir.com/game-dev/trss"
DEFAULT_HEADERS = {"Content-Type": "application/json", "User-Agent": ""}

def make_request(sub: str, action: str, data: dict = {}, headers: dict = DEFAULT_HEADERS, url: str = DEFAULT_URL) -> dict:
    """Make POST request to url/sub/action with given data and headers."""
    response = requests.post(f"{url}/{sub}/{action}", json=data, headers=headers)
    return response.json()

def make_auth_request(token: str, sub: str, action: str, data: dict = {}, headers: dict = DEFAULT_HEADERS, url: str = DEFAULT_URL) -> dict:
    """Same as make_request(), but for actions that require token."""
    headers["user-token"] = token
    return make_request(sub, action, data, headers, url)
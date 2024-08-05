import requests
DEFAULT_URL = "https://iamtagir.com/game-dev/trss"
DEFAULT_HEADERS = {"Content-Type": "application/json", "User-Agent": ""}
# base

def make_request(sub: str, action: str, data: dict = {}, headers: dict = DEFAULT_HEADERS, url: str = DEFAULT_URL) -> dict:
    """Make POST request to <url>/<sub>/<action> with given data and headers."""
    response = requests.post(f"{url}/{sub}/{action}", json=data, headers=headers)
    return response.json()

def make_authorized_request(token: str, sub: str, action: str, data: dict = {}, headers: dict = DEFAULT_HEADERS, url: str = DEFAULT_URL) -> dict:
    """Same as make_request(), but for actions that require token."""
    headers["user-token"] = token
    return make_request(sub, action, data, headers, url)


# users

def login(login_: str, password: str) -> dict:
    """Log into TR account and return the user's token."""
    return make_request("users", "login", {"login": login_, "password": password})

def get_by_id(id_: int) -> dict:
    """Get user by their TRSS id."""
    return make_request("users", "getById", {"id":id_})

def get_by_token(token: str) -> dict:
    """Get user by their token. Token required."""
    return make_authorized_request(token, "users", "getByToken", {})

def change_skin(token: str, skin: str, primary_color: str, secondary_color: str) -> dict:
    """Change the main skin of user and return it. Token required."""
    return make_authorized_request(token, "users", "changeSkin", {"skin": skin, "primaryColor": primary_color, "secondaryColor": secondary_color})

def change_nick(token: str, nick: str) -> dict:
    """Change the user's nickname. Token required."""
    return make_authorized_request(token, "users", "changeNick", {"nick":nick})

def toggle_like(token: str, skin_id: int) -> dict:
    """Toggle the user's like on skin. Token required."""
    return make_authorized_request(token, "users", "toggleLike", {"skinId":  skin_id})

def register_view(token: str, skin_id: int):
    """Register that the user has seen the skin. Token required."""
    return make_authorized_request(token, "users", "registerView", {"skinId": skin_id})

def get_like(skin_id: int, user_id: int):
    """Check if the user liked the skin."""
    return make_request("users", "getLike", {"skinId": skin_id, "userId": user_id})


# skins

def upload(token: str, skin: str, primary_color: str, secondary_color: str, name: str):
    """Upload skin. Token required."""
    return make_authorized_request(token, "skins", "upload", {"skin": skin, "primaryColor": primary_color, "secondaryColor": secondary_color, "name": name})

def delete(token: str, skin_id: int): 
    """Delete skin. Token required."""
    return make_authorized_request(token, "skins", "delete", {"id":skin_id})

def get_one_by_id(skin_id: int):
    """Get skin by its ID."""
    return make_request("skins", "getOneById", data={"id": skin_id})

def get_a_lot(from_id: int, amount: int, order_by: str):
    """Get <amount> of skins from <from_id> in specific order.

    Order options:
    "older" - from lowest id to highest,
    "fresher" - from highest id to lowest,
    "mostLikes" - from most liked to least liked,
    "mostViews" - from most viewed to least viewed.
    """
    return make_request("skins", "getALot", {"fromId": from_id, "amount": amount, "orderBy": order_by})

def get_by_author(author_id: int, amount: int):
    """Get last [amount] skins from the author."""
    return make_request("skins", "getByAuthor", {"id": author_id, "amount": amount})

def get_count(skin_id: int, count_of: str):
    """Get amount of likes or views of skin.
     
    count_of == "likes" -> return amount of likes,\n
    count_of == "views" -> return amount of views.
    """
    return make_request("skins", "getCount", {"id": skin_id, "countOf": count_of})

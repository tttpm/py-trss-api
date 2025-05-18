from . import base

def login(login_: str, password: str) -> dict:
    """Log into TRSS account using TR login and password and return the user's token."""
    return base.make_request("users", "login", {"login": login_, "password": password})

def get_by_id(id: int) -> dict:
    """Get user by their TRSS id."""
    return base.make_request("users", "getById", {"id":id})

def get_by_token(token: str) -> dict:
    """Get user by their token. Token required."""
    return base.make_auth_request(token, "users", "getByToken", {})

def change_skin(token: str, skin: str, primary_color: str, secondary_color: str) -> dict:
    """Change skin of the user and return it. primary_color and secondary_color are colors of looper's body and punts respectively. Token required."""
    return base.make_auth_request(token, "users", "changeSkin", {"skin": skin, "primaryColor": primary_color, "secondaryColor": secondary_color})

def change_nick(token: str, nick: str) -> dict:
    """Change the user's nickname. Token required."""
    return base.make_auth_request(token, "users", "changeNick", {"nick": nick})

def toggle_like(token: str, skin_id: int) -> dict:
    """Toggle the user's like on skin. Token required."""
    return base.make_auth_request(token, "users", "toggleLike", {"skinId":  skin_id})

def register_view(token: str, skin_id: int):
    """Register that the user has viewed the skin. Token required."""
    return base.make_auth_request(token, "users", "registerView", {"skinId": skin_id})

def get_like(skin_id: int, user_id: int):
    """Check if the user liked the skin."""
    return base.make_request("users", "getLike", {"skinId": skin_id, "userId": user_id})


from . import base

def upload(token: str, skin: str, primary_color: str, secondary_color: str, name: str) -> dict:
    """Upload skin. primary_color and secondary_color are colors of looper's body and punts respectively. Token required."""
    return base.make_auth_request(token, "skins", "upload", {"skin": skin, "primaryColor": primary_color, "secondaryColor": secondary_color, "name": name})

def delete(token: str, id: int) -> dict: 
    """Delete skin. Token required."""
    return base.make_auth_request(token, "skins", "delete", {"id":id})

def get_one_by_id(id: int) -> dict:
    """Get skin by its ID."""
    return base.make_request("skins", "getOneById", data={"id": id})

def get_a_lot(order_by: str, from_: int, amount: int) -> list[dict]:
    """Get [amount] of skins in specified order, starting from [from_id] skin in that order.

    Order options: \n
    "older" - from lowest id to highest, \n
    "fresher" - from highest id to lowest, \n
    "mostLikes" - from most liked to least liked, \n
    "mostViews" - from most viewed to least viewed. \n
    """
    return base.make_request("skins", "getALot", {"from": from_, "amount": amount, "orderBy": order_by})

def get_by_author(id: int, from_: int, amount: int) -> list[dict]:
    """Get [amount] last skins from the author, starting from [from_id] in "older" order."""
    return base.make_request("skins", "getByAuthor", {"from": from_, "id": id, "amount": amount})

def get_count(id: int, count_of: str) -> dict:
    """Get amount of likes or views on a skin.
     
    count_of == "likes" -> return amount of likes,\n
    count_of == "views" -> return amount of views.
    """
    return base.make_request("skins", "getCount", {"id": id, "countOf": count_of})

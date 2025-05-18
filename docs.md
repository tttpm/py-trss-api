# Value types

**string** - just a string

**token** - TRSS token

**int** - integer number

**bool** - 0 or 1

**hex** - six-character hexadecimal representation of HTML color (e. g. "e6ac0c")

**skin** - Team Run skin in trSkin1 format

**Each function (except for two) returns a dictionary with specified fields, or, if request was unsuccessful, a dictionary with only field "error"**

# trssapi.users

## login(login_: str, password: str)

### Description
Log into TRSS account. Note that TRSS uses Team Run logins and passwords.

### Parameters
**login_** (string) - Team Run account login

**password** (string)- Team Run account password

### Returns 

**token** (token) - user's token

**first** (bool) - is user logged in for first time


## get_by_id(id: int)

### Description
Get user by their TRSS id.

### Parameters
**id** (int) - user's TRSS id

### Returns 

**id** (int) - user's TRSS id

**login** (int) - user's TR login

**nick** (string) - users's TRSS nickname (equals to login by default)

**skin** (skin) - user's skin 

**primaryColor** (hex) - user's "head" color

**secondaryColor** (hex) - user's "pants" color

**moderator** (bool) - is user a TRSS moderator

**muted** (bool) - is user muted

**until** (int/None) - muted until that time, if muted; else None

## get_by_token(token: str)

### Description
Get user by their TRSS token.

### Parameters
**token** (token) - user's TRSS token

### Returns 

**id** (int) - user's TRSS id

**login** (int) - user's TR login

**token** (token) - user's TRSS token

**nick** (string) - users's TRSS nickname (equals to login by default)

**skin** (skin) - user's skin 

**primaryColor** (hex) - user's "head" color

**secondaryColor** (hex) - user's "pants" color

**moderator** (bool) - is user a TRSS moderator

**muted** (bool) - is user muted

**until** (int/None) - muted until that time, if muted; else None

## change_skin(token: str, skin: str, primary_color: str, secondary_color: str)

### Description
Change skin of the user.

### Parameters
**token** (token) - user's TRSS token

**skin** (skin) - new skin in trSkin1 format 

**primary_color** (hex) - new looper's "head" color

**secondary_color** (hex) - new looper's "pants" color

### Returns 

**skin** (skin) - skin in trSkin1 format 

**primary_color** (hex) - looper's "head" color

**secondary_color** (hex) - looper's "pants" color 

## change_nick(token: str, nick: str)

### Description
Change TRSS nickname of the user.

### Parameters
**token** (token) - user's TRSS token

**nick** (string) - new nickname

### Returns 

**nick** (string) - nickname

## toggle_like(token: str, skin_id: int)

### Description
Toggle user's like on skin (if user liked it before, unlike it; else like it)

### Parameters
**token** (token) - user's TRSS token

**skin_id** (int) - id of the skin

### Returns 

**state** (bool) - is skin liked

## register_view(token: str, skin_id: int)

### Description
Register that user has viewed the skin.

### Parameters
**token** (token) - user's TRSS token

**skin_id** (int) - id of the skin

### Returns 

**state** (bool) - is skin viewed for the first time

## get_like(skin_id: int, user_id: int)

### Description
Check if the user has liked the skin.

### Parameters
**skin_id** (int) - id of the skin

**user_id** (int) - user's TRSS id

### Returns 

**state** (bool) - has user liked the skin

# trssapi.skins

## upload(token: str, skin: str, primary_color: str, name: str)

### Description
Upload a skin to TRSS.

### Parameters
**token** (token) - user's TRSS token

**skin** (skin) - skin to upload

**primary_color** (hex) - looper's "head" color

**secondary_color** (hex) - looper's "pants" color

**name** (string) - name of the skin

### Returns 

**state** (bool) - was skin uploaded successfully

## delete(token: str, id: int)

### Description
Delete skin from TRSS.

### Parameters
**token** (token) - user's TRSS token

**id** (int) - id of the skin

### Returns 

**state** (bool) - was skin deleted successfully


## get_one_by_id(id: int)

### Description
Get skin by its id.

### Parameters
**id** (int) - id of the skin

### Returns 

**id** (int) - id of the skin

**name** (string) - name of the skin

**author** (int) - author's TRSS id

**skin** (skin) - skin

**primaryColor** (hex) - looper's "head" color

**secondaryColor** (hex) - looper's "pants" color


## get_a_lot(order_by: str, from_: int, amount: int)

### Description
Get list of skins in specified order.

### Parameters
**order_by** (string) - order in which skins should be listed.
There are four options for that parameter:
1. **"older"** - from lowest id to highest
2. **"fresher"** - from highest id to lowest
3. **"mostLikes"** - from most liked to least liked
4. **"mostViews"** - from most viewed to least viewed

**from_** (int) - position in this list to start from

**amount** (int) - amount of skins to be returned.

### Returns 

**This function returns list of dicts; each dict contains:**

**id** (int) - id of the skin

**name** (string) - name of the skin

**author** (int) - author's TRSS id

**skin** (skin) - skin

**primaryColor** (hex) - looper's "head" color

**secondaryColor** (hex) - looper's "pants" color

## get_by_author(id: int, from_: int, amount: int)

### Description
Get list of skins posted by given author. Skins are listed in "older" order (from lowest id to highest).

### Parameters
**id** (int) - author's TRSS id

**from_** (int) - position in this list to start from

**amount** (int) - amount of skins to be returned.

### Returns 

**This function returns list of dicts; each dict contains:**

**id** (int) - id of the skin

**name** (string) - name of the skin

**author** (int) - author's TRSS id

**skin** (skin) - skin

**primaryColor** (hex) - looper's "head" color

**secondaryColor** (hex) - looper's "pants" color

## get_count(id: int, count_of: str)

### Description
Get amount of likes or views on a skin.

### Parameters
**id** (int) - skin id

**count_of** (string) - value to get count of. There are two options for this parameter:

1. **"likes"** - return amount of likes
2. **"views"** - return amount of views

### Returns 

**count** (int) - requested count
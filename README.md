# py-trss-api

py-trss-api is a simple module for interaction with Team Run Skin Storage database.

Team Run Skin Storage is an incredible app for saving and sharing IamTagir's Team Run game skins, made by aumnlify.

## Usage

The module consists of two submodules: `users` and `skins`, for users-related and skins-related actions respectively. 

Usage is quite simple:

```python
>>> from trssapi.users import get_by_id
>>> from trssapi.skins import get_one_by_id
>>> get_by_id(6)
{'id': 6, 'login': 'DKorj', 'nick': 'Дкоржака', 'skin': 'trSkin17ZTbroMgEEV/aeQiND6BwP9/0sHSbtGxVHNsHxpNTFZGRtZGkKhcA11wwQU/AZ2k1LmUZjhr8OfAmptw/qgzuvZMIbwMOtXwT+dRJpXyNeQ7xjcaGIOu/c558CwfpTOUKzKSU/nZ0OdyWQ3/6JrBkOxMfuSIBIk23MLUU79nDJ27VwBRC70C40IvlkmJpJ5UO0HK1qoAHUhLsZB/qnLwgcx9LsCGxmtAF0+BpFjVxjrDmQNSNGAerEkIU8Oe7BvObD/3WjkzH6JcgbwaSYnpW+iYNeRCg6liij25ANhIpX1zQ/IdbrT1zpVDlNIiBcbwysZW/xgUwxpin/zz4BdnpOC5ijxSfMd5Wv5ky2+nGLoYKNjaGSngjEpQMUW7+n2VrkPQNOSwdoYGT4EuVM5y5rCl+hKqrkec033OUm18gkau89bnQNcf', 'primaryColor': '000cba', 'secondaryColor': '000000', 'moderator': 1, 'muted': 0, 'until': None}
>>> get_one_by_id(42)
{'id': 42, 'name': 'Defective looper', 'author': 6, 'skin': 'trSkin17ZJRCoAgEAWvtKal0pdZ3v9IsaVFEGJpKZbv482CwqACrKuHH3KDoJhSbGoQ/Zgxo5jUW5+yzQtSaK5NKTYhQAzm5uHXv0aUbRYQXE1GlmLjgxGzVcCJQWJ6uiw32SIa46ZItZYwBY2r64aqZQQ6J2rVkhrucPkWN7B6p5a2klneAt8LHyuv5w/1wQw=', 'primaryColor': '757575', 'secondaryColor': '292929', 'likes': 1, 'views': 9}
```
### Tokens 

Some actions require authentication with *token* - unique user identifier. To get one, use `users.login()`.
```py
>>> from trssapi.users import login, register_view
>>> login_response = login("login", "password")
>>> login_response
{'token': 'your-token-here', 'first': 0}
>>> token = login_response["token"]
>>> register_view(token, 42)
{'state': 1}
```

You can see full documentation in docs.md file.
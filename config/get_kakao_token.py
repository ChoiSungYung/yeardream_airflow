import requests
# client_id, authorize_code 노출 주의, 실제 값은 임시로만 넣고 Git에 올라가지 않도록 유의

client_id = '67b0ec369140507bc792c9e460a26e91'
redirect_uri = 'https://example.com/oauth'
authorize_code = 'H4Xpp1K9-p3pJf5EiIgNuJFu174pz3uyBFSU8_K--2GM6zFeqYDCgwAAAAQKPXLqAAABkC3zEzJPBWDH3LuH7A'


token_url = 'https://kauth.kakao.com/oauth/token'
data = {
    'grant_type': 'authorization_code',
    'client_id': client_id,
    'redirect_uri': redirect_uri,
    'code': authorize_code,
    }

response = requests.post(token_url, data=data)
tokens = response.json()
print(tokens)
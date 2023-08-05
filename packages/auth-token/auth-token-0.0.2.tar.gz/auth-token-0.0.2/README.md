# Auth-token

Package Auth token jwt

## Package installation
- Installation
    ```shell
    $ pip3 install auth-token
    ```

## Docs
```python

>>> from auth_token import AuthToken

>>> identifier = '12345678'
>>> exp_minutes = 60
>>> secret_key = 'secret_key'
>>> auth = AuthToken(identifier, exp_minutes, secret_key)
>>> response = auth.encode()
>>> print(response.token)
'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1ODc5NTY5ODQsImlhdCI6MTU4Nzk1NjY4NCwic3ViIjoiMSIsInV1aWQiOiJhYTUwNWE3ZS1hMjEyLTRiOTktYmI3Yy02Njg3MjViZGQ3YTcifQ.l1uGXiZpZHuOt0iWmcksLsdkUQjYesH_OxmCpjJHWDk'
```

[Edit in Gitlab](https://gitlab.com/developerjoseph/auth-token)
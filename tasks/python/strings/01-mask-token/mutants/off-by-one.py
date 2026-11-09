def mask_token(token: str) -> str:
    if len(token) <= 5:
        return token
    return "*" * (len(token) - 5) + token[-5:]

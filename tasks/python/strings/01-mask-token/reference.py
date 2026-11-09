def mask_token(token: str) -> str:
    if len(token) <= 4:
        return token
    return "*" * (len(token) - 4) + token[-4:]

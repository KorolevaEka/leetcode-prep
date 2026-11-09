def mask_token(token: str) -> str:
    if len(token) <= 4:
        return token
    return token[:-4] + "*" * 4

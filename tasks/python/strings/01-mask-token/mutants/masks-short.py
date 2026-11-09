def mask_token(token: str) -> str:
    return "*" * max(len(token) - 4, 0) + token[-4:] if len(token) > 4 else "*" * len(token)

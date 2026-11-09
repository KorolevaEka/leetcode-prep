def is_strong_password(password: str) -> bool:
    return (
        len(password) >= 7
        and any(ch.isdigit() for ch in password)
        and any(ch.isupper() for ch in password)
    )

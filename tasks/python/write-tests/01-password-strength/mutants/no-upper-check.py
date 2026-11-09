def is_strong_password(password: str) -> bool:
    return (
        len(password) >= 8
        and any(ch.isdigit() for ch in password)
    )

def email_domain(email: str) -> str:
    email = email.strip().lower()
    if "@" not in email:
        return ""
    return email.partition("@")[2]

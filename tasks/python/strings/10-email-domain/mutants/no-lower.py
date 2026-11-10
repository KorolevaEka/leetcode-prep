def email_domain(email: str) -> str:
    email = email.strip()
    if email.count("@") != 1:
        return ""
    return email.partition("@")[2]

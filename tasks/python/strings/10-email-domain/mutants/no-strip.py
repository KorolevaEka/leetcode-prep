def email_domain(email: str) -> str:
    email = email.lower()
    if email.count("@") != 1:
        return ""
    return email.partition("@")[2]

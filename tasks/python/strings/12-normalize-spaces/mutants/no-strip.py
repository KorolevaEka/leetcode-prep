def clean_message(text: str) -> str:
    import re
    return re.sub(r"\s+", " ", text)

def clean_message(text: str) -> str:
    return " ".join(p for p in text.split(" ") if p)

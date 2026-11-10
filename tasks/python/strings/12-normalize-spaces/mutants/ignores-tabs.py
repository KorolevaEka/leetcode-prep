def clean_message(text: str) -> str:
    return " ".join(p for p in text.replace("\n", " ").replace("\r", " ").split(" ") if p)

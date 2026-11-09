def is_balanced(selector: str) -> bool:
    return (selector.count("(") == selector.count(")")
            and selector.count("[") == selector.count("]")
            and selector.count("{") == selector.count("}"))

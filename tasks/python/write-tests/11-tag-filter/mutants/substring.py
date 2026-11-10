def has_tag(tags, wanted):
    return any((wanted.strip().casefold() in x.strip().casefold() for x in tags))

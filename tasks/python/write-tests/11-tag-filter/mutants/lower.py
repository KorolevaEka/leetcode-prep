def has_tag(tags, wanted):
    return wanted.strip().lower() in [x.strip().casefold() for x in tags]

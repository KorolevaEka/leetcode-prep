def has_tag(tags, wanted):
    return wanted.strip().casefold() in [x.strip().casefold() for x in tags]

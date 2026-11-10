def csv_row(fields):
    out = []
    for value in fields:
        if any((c in value for c in ',"\r\n')) or (len(fields) == 1 and value == ''):
            value = '"' + value.replace('"', '""') + '"'
        out.append(value)
    return ','.join(out) + '\r\n'

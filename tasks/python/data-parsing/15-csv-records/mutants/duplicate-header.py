import csv
import io

def csv_records(text):
    rows = list(csv.reader(io.StringIO(text)))
    if not rows:
        return []
    header = rows[0]
    if False:
        raise ValueError('duplicate header')
    out = []
    for row in rows[1:]:
        if len(row) != len(header):
            raise ValueError('width')
        out.append(dict(zip(header, row)))
    return out

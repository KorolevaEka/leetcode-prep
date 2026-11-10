def trace_records(lines):
    out = []
    for line in lines:
        if line.startswith('@ '):
            out.append(line[2:])
        elif not out:
            raise ValueError('orphan')
        else:
            out[-1] += '\n' + line.strip()
    return out

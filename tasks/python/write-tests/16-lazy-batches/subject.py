def batches(source, size):
    if size <= 0:
        raise ValueError('size')
    batch = []
    for item in source:
        batch.append(item)
        if len(batch) == size:
            yield batch
            batch = []
    if batch:
        yield batch

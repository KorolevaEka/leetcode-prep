def batch_count(total, size):
    if total < 0 or size <= 0:
        raise ValueError('arguments')
    return total // size

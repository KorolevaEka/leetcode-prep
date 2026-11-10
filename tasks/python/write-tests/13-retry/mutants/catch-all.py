def retry(operation, attempts):
    if attempts < 1:
        raise ValueError('attempts')
    for i in range(attempts):
        try:
            return operation()
        except Exception:
            if i == attempts - 1:
                raise

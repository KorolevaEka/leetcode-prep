def retry(operation, attempts):
    if attempts < 1:
        raise ValueError('attempts')
    for i in range(attempts - 1):
        try:
            return operation()
        except ValueError:
            if i == attempts - 1:
                raise

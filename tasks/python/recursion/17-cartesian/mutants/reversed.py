def parameter_matrix(axes):
    if not axes:
        return [[]]
    return [tail + [x] for x in axes[0] for tail in parameter_matrix(axes[1:])]

def parameter_matrix(axes):
    if not axes:
        return [[]]
    return [[x] + tail for x in axes[0] for tail in parameter_matrix(axes[1:])]

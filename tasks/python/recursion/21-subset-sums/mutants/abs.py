def subset_sums(costs):

    def visit(i):
        if i == len(costs):
            return {0}
        tail = visit(i + 1)
        return tail | {abs(costs[i]) + x for x in tail}
    return sorted(visit(0))

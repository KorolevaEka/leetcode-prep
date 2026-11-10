def inversion_count(ids):
    return sum(ids[i]>ids[j] for i in range(len(ids)) for j in range(i+1,len(ids)))
